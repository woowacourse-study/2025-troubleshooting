#!/usr/bin/env python3
"""Publish one generated commit, merging data rather than rebasing generated text.

Retries use disposable worktrees. The original commit is retained on failure;
no force push, reset of the caller, or conflict-marker resolution is performed.
"""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time

import yaml

MISSING = object()
DATA = ".automation/weeks.yml"


class Conflict(RuntimeError):
    pass


def merge(base, local, remote, path=()):
    if local == base or local == remote:
        return remote
    if remote == base:
        return local
    if isinstance(local, dict) and isinstance(remote, dict) and (isinstance(base, dict) or base is MISSING):
        base = {} if base is MISSING else base
        result = {}
        for key in dict.fromkeys([*remote, *local, *base]):
            value = merge(base.get(key, MISSING), local.get(key, MISSING), remote.get(key, MISSING), (*path, str(key)))
            if value is not MISSING:
                result[key] = value
        return result
    if isinstance(local, list) and isinstance(remote, list) and (isinstance(base, list) or base is MISSING):
        field = path[-1] if path else ""
        if field not in ("weeks", "presentations"):
            raise Conflict("Concurrent list edits: " + "/".join(path))
        def keyed(items):
            result = {}
            for item in items:
                key = item["week"] if field == "weeks" else item.get("pdf") or (item["presenter"], item["title"])
                if key in result:
                    raise Conflict("Duplicate identity: " + repr(key))
                result[key] = item
            return result
        merged = merge(keyed([] if base is MISSING else base), keyed(local), keyed(remote), path)
        values = list(merged.values())
        return sorted(values, key=lambda w: w["week"]) if field == "weeks" else values
    raise Conflict("Concurrent edits require review: " + "/".join(path))


def git(root, *args, check=True):
    return subprocess.run(["git", "-C", str(root), *args], check=check, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def text(root, *args):
    return git(root, *args).stdout.decode("utf-8").strip()


def entry(root, ref, path):
    return git(root, "ls-tree", ref, "--", ":(literal)" + path).stdout


def publish(root: Path, attempts=8, delay=2):
    root = root.resolve()
    if git(root, "status", "--porcelain").stdout:
        raise Conflict("Commit all generated changes before publishing")
    original = text(root, "rev-parse", "HEAD")
    base = text(root, "rev-parse", "HEAD^")
    message = text(root, "log", "-1", "--format=%B")
    candidate = original
    for attempt in range(1, attempts + 1):
        pushed = git(root, "push", "origin", candidate + ":refs/heads/main", check=False)
        if pushed.returncode == 0:
            return candidate
        print(pushed.stderr.decode("utf-8", errors="replace"), file=sys.stderr)
        git(root, "fetch", "origin", "main")
        remote = text(root, "rev-parse", "FETCH_HEAD")
        # A lost HTTP response may hide a successful push.
        if git(root, "merge-base", "--is-ancestor", candidate, remote, check=False).returncode == 0:
            return candidate
        if attempt == attempts:
            raise Conflict(f"Push failed after {attempts} attempts; original commit retained: {original}")
        if remote == base:
            raise Conflict("Push rejected without an upstream change; check permissions/branch rules")
        print(f"Push attempt {attempt} rejected; merging generated data onto {remote}")
        with tempfile.TemporaryDirectory(prefix="generated-push-") as directory:
            tree = Path(directory) / "tree"
            git(root, "worktree", "add", "--detach", str(tree), remote)
            try:
                data = [yaml.safe_load(git(root, "show", ref + ":" + DATA).stdout) for ref in (base, original, remote)]
                combined = merge(*data)
                (tree / DATA).write_text(yaml.safe_dump(combined, allow_unicode=True, sort_keys=False, width=1000), encoding="utf-8")
                paths = git(root, "diff", "--name-only", "--no-renames", "-z", base, original).stdout.decode("utf-8").split("\0")
                for path in filter(None, paths):
                    if path in (DATA, "README.md"):
                        continue
                    before, wanted, current = [entry(root, ref, path) for ref in (base, original, remote)]
                    if current == wanted:
                        continue
                    if current != before:
                        raise Conflict("Concurrent file edits require review: " + path)
                    git(tree, "restore", "--source=" + original, "--staged", "--worktree", "--", ":(literal)" + path)
                env = {**os.environ, "PYTHONUTF8": "1"}
                subprocess.run([sys.executable, str(tree / ".automation/scripts/generate_readme.py")], cwd=tree, env=env, check=True)
                git(tree, "add", "--", DATA, "README.md")
                if git(tree, "diff", "--cached", "--quiet", check=False).returncode == 0:
                    return remote
                git(tree, "commit", "-m", message)
                candidate = text(tree, "rev-parse", "HEAD")
            finally:
                git(root, "worktree", "remove", "--force", str(tree))
        time.sleep(delay)
    raise AssertionError("unreachable")


def main():
    try:
        published = publish(Path.cwd())
        output = os.environ.get("GITHUB_OUTPUT")
        if output:
            with open(output, "a", encoding="utf-8") as stream:
                stream.write("committed=true\n")
        print("Published generated changes: " + published)
        return 0
    except (Conflict, subprocess.CalledProcessError, OSError, yaml.YAMLError) as error:
        print(str(error), file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr.decode("utf-8", errors="replace"), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
