import copy
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest
from unittest.mock import patch

import yaml

SCRIPTS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("push_generated", SCRIPTS / "push_generated.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def run(root, *args, check=True):
    return subprocess.run(["git", "-C", str(root), *args], check=check, capture_output=True)


def data(*names):
    return {"weeks": [{"week": 23, "date": "2026-09-08", "presentations": [
        {"presenter": n, "title": n, "pdf": n + ".pdf", "thumbnail": n + ".png", "youtube": None}
        for n in names]}]}


class MergeTests(unittest.TestCase):
    def test_disjoint_fields_and_deletion(self):
        base=data("A", "B")
        local=copy.deepcopy(base); local["weeks"][0]["presentations"].pop()
        remote=copy.deepcopy(base); remote["weeks"][0]["presentations"][0]["youtube"]="video"
        result=m.merge(base,local,remote)
        self.assertEqual(len(result["weeks"][0]["presentations"]),1)
        self.assertEqual(result["weeks"][0]["presentations"][0]["youtube"],"video")

    def test_conflict_and_delete_modify(self):
        base=data("A"); local=copy.deepcopy(base); remote=copy.deepcopy(base)
        local["weeks"][0]["presentations"][0]["youtube"]="left"
        remote["weeks"][0]["presentations"][0]["youtube"]="right"
        with self.assertRaises(m.Conflict): m.merge(base,local,remote)
        with self.assertRaises(m.Conflict): m.merge(base,data(),remote)

    def test_concurrent_new_week_and_idempotency(self):
        combined=m.merge({"weeks":[]},data("A"),data("B"))
        self.assertEqual({p["presenter"] for p in combined["weeks"][0]["presentations"]},{"A","B"})
        self.assertEqual(m.merge(data(),data("A"),data("A")),data("A"))


class GitTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory(); self.addCleanup(self.tmp.cleanup)
        self.root=Path(self.tmp.name); self.remote=self.root/"remote.git"
        run(self.root,"init","--bare",str(self.remote))
        self.a=self.root/"a"; run(self.root,"clone",str(self.remote),str(self.a))
        run(self.a,"switch","-c","main")
        self.configure(self.a)
        (self.a/".automation/scripts").mkdir(parents=True)
        (self.a/".automation/templates").mkdir()
        shutil.copyfile(SCRIPTS/"generate_readme.py",self.a/".automation/scripts/generate_readme.py")
        (self.a/".automation/templates/readme_header.md").write_text("# Study",encoding="utf-8")
        self.write(self.a,data())
        self.commit(self.a,"base"); run(self.a,"push","-u","origin","main")
        self.b=self.root/"b"; run(self.root,"clone","-b","main",str(self.remote),str(self.b)); self.configure(self.b)

    def configure(self,repo):
        run(repo,"config","user.name","Test"); run(repo,"config","user.email","test@example.invalid")

    def write(self,repo,value):
        (repo/".automation/weeks.yml").write_text(yaml.safe_dump(value,allow_unicode=True,sort_keys=False),encoding="utf-8")
        subprocess.run([m.sys.executable,str(repo/".automation/scripts/generate_readme.py")],env={**os.environ,"PYTHONUTF8":"1"},check=True,capture_output=True)

    def commit(self,repo,message):
        run(repo,"add","."); run(repo,"commit","-m",message)

    def uploads(self):
        for repo,name in ((self.a,"A"),(self.b,"B")):
            self.write(repo,data(name))
            (repo/(name+".pdf")).write_bytes(b"%PDF-1.4\x00"+name.encode())
            (repo/(name+".png")).write_bytes(b"PNG\x00"+name.encode())
            self.commit(repo,"upload "+name)
        run(self.b,"push","origin","main")

    def test_reproduce_original_rebase_conflict_then_preserve_both_uploads(self):
        self.uploads()
        run(self.a,"fetch","origin","main")
        failed=run(self.a,"rebase","origin/main",check=False)
        self.assertNotEqual(failed.returncode,0)
        conflicts=run(self.a,"diff","--name-only","--diff-filter=U").stdout.decode()
        self.assertIn(".automation/weeks.yml",conflicts); self.assertIn("README.md",conflicts)
        run(self.a,"rebase","--abort")
        original=m.text(self.a,"rev-parse","HEAD")
        published=m.publish(self.a,delay=0)
        self.assertEqual(m.text(self.a,"rev-parse","HEAD"),original)
        merged=yaml.safe_load(run(self.remote,"show","main:.automation/weeks.yml").stdout)
        self.assertEqual({p["presenter"] for p in merged["weeks"][0]["presentations"]},{"A","B"})
        for name in ("A","B"):
            self.assertEqual(run(self.remote,"show","main:"+name+".pdf").stdout,b"%PDF-1.4\x00"+name.encode())
            self.assertIn((name+".pdf").encode(),run(self.remote,"show","main:README.md").stdout)
        self.assertEqual(m.text(self.remote,"rev-parse","main"),published)
        self.assertEqual(len(run(self.a,"worktree","list","--porcelain").stdout.split(b"worktree "))-1,1)

    def test_conflict_keeps_original_and_remote_and_cleans_worktree(self):
        self.uploads()
        # Independently different contents for the same newly created path.
        (self.b/"A.pdf").write_bytes(b"other person's file")
        self.commit(self.b,"conflicting file"); run(self.b,"push","origin","main")
        before=m.text(self.remote,"rev-parse","main"); original=m.text(self.a,"rev-parse","HEAD")
        with self.assertRaises(m.Conflict): m.publish(self.a,delay=0)
        self.assertEqual(m.text(self.remote,"rev-parse","main"),before)
        self.assertEqual(m.text(self.a,"rev-parse","HEAD"),original)
        self.assertEqual(len(run(self.a,"worktree","list","--porcelain").stdout.split(b"worktree "))-1,1)

    def test_retry_exhaustion_and_dirty_checkout(self):
        self.uploads()
        with self.assertRaises(m.Conflict): m.publish(self.a,attempts=1,delay=0)
        (self.a/"uncommitted.txt").write_text("keep")
        with self.assertRaises(m.Conflict): m.publish(self.a,delay=0)
        self.assertEqual((self.a/"uncommitted.txt").read_text(),"keep")

    def test_direct_success(self):
        self.write(self.a,data("A")); self.commit(self.a,"upload")
        self.assertEqual(m.publish(self.a,delay=0),m.text(self.a,"rev-parse","HEAD"))

    def test_another_writer_wins_during_retry(self):
        self.uploads()
        real_git=m.git
        pushes=0
        def racing_git(root,*args,**kwargs):
            nonlocal pushes
            if args[0]=="push":
                pushes+=1
                if pushes==2:
                    self.write(self.b,data("B","C")); self.commit(self.b,"third upload")
                    run(self.b,"push","origin","main")
            return real_git(root,*args,**kwargs)
        with patch.object(m,"git",side_effect=racing_git): m.publish(self.a,delay=0)
        merged=yaml.safe_load(run(self.remote,"show","main:.automation/weeks.yml").stdout)
        self.assertEqual({p["presenter"] for p in merged["weeks"][0]["presentations"]},{"A","B","C"})
        self.assertEqual(pushes,3)

    def test_rollback_preserves_other_upload(self):
        self.write(self.a,data("A")); (self.a/"A.pdf").write_bytes(b"%PDF")
        self.commit(self.a,"seed A"); run(self.a,"push","origin","main")
        run(self.b,"pull","--ff-only","origin","main")
        self.write(self.a,data()); run(self.a,"rm","A.pdf"); self.commit(self.a,"rollback A")
        self.write(self.b,data("A","B")); self.commit(self.b,"upload B"); run(self.b,"push","origin","main")
        m.publish(self.a,delay=0)
        merged=yaml.safe_load(run(self.remote,"show","main:.automation/weeks.yml").stdout)
        self.assertEqual([p["presenter"] for p in merged["weeks"][0]["presentations"]],["B"])
        self.assertEqual(run(self.remote,"ls-tree","main","--","A.pdf").stdout,b"")

    def test_generator_failure_cleans_worktree_without_push(self):
        self.uploads()
        before=m.text(self.remote,"rev-parse","main")
        real_run=subprocess.run
        def failing_run(command,*args,**kwargs):
            if str(command[0])==m.sys.executable:
                raise subprocess.CalledProcessError(1,command,stderr=b"generator failed")
            return real_run(command,*args,**kwargs)
        with patch.object(m.subprocess,"run",side_effect=failing_run):
            with self.assertRaises(subprocess.CalledProcessError): m.publish(self.a,delay=0)
        self.assertEqual(m.text(self.remote,"rev-parse","main"),before)
        self.assertEqual(len(run(self.a,"worktree","list","--porcelain").stdout.split(b"worktree "))-1,1)


if __name__ == "__main__": unittest.main()
