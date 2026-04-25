#!/usr/bin/env python3
"""
PDF 발표자료의 첫 페이지를 PNG 썸네일로 추출한다.

입력: weeks.yml (repo root)
출력: .automation/thumbnails/w{week:02d}_{slug}.png

규칙
- `thumbnail:` 필드가 비어있거나 로컬 `.automation/thumbnails/` 경로일 때만 자동 생성
- 이미 생성된 썸네일이 존재하고 원본 PDF보다 최신이면 스킵

의존성: poppler-utils (`pdftoppm`)
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml


# Script lives at .automation/scripts/; repo root is two levels up.
ROOT = Path(__file__).resolve().parent.parent.parent
THUMB_DIR = ROOT / ".automation" / "thumbnails"
THUMB_REL_PREFIX = ".automation/thumbnails"
DATA_FILE = ROOT / "weeks.yml"


def slugify(presenter: str, title: str) -> str:
    # Use presenter as primary key (unique within a week)
    s = re.sub(r"[^0-9A-Za-z가-힣]+", "_", presenter).strip("_")
    return s or "unknown"


def needs_rebuild(png: Path, pdf: Path) -> bool:
    if not png.exists():
        return True
    return png.stat().st_mtime < pdf.stat().st_mtime


def extract_first_page(pdf: Path, out_png: Path) -> bool:
    out_png.parent.mkdir(parents=True, exist_ok=True)
    # -singlefile suppresses the page-number suffix so output is exactly {prefix}.png
    prefix = out_png.with_suffix("")
    cmd = ["pdftoppm", "-png", "-r", "150", "-singlefile", "-f", "1", "-l", "1", str(pdf), str(prefix)]
    try:
        subprocess.run(cmd, check=True, capture_output=True)
    except FileNotFoundError:
        print("error: pdftoppm not found. Install poppler-utils.", file=sys.stderr)
        return False
    except subprocess.CalledProcessError as e:
        print(f"error: pdftoppm failed for {pdf}: {e.stderr.decode(errors='replace')}", file=sys.stderr)
        return False
    return out_png.exists()


def main() -> int:
    with DATA_FILE.open() as f:
        data = yaml.safe_load(f)

    generated = 0
    skipped = 0
    warnings = 0

    for week in data["weeks"]:
        wk = week["week"]
        for pres in week["presentations"]:
            pdf_rel = pres.get("pdf")
            thumb = pres.get("thumbnail")

            # Keep external thumbnails as-is (user-attachments etc.)
            if thumb and not thumb.startswith(THUMB_REL_PREFIX):
                continue

            if not pdf_rel:
                continue

            pdf_path = ROOT / unicodedata.normalize("NFC", pdf_rel)
            if not pdf_path.exists():
                print(f"warn: missing pdf for week {wk} / {pres['presenter']}: {pdf_rel}", file=sys.stderr)
                warnings += 1
                continue

            slug = slugify(pres["presenter"], pres["title"])
            out_png = THUMB_DIR / f"w{wk:02d}_{slug}.png"
            thumb_rel = f"{THUMB_REL_PREFIX}/{out_png.name}"

            if not needs_rebuild(out_png, pdf_path):
                # Re-sync yml even when the PNG is up-to-date, in case a prior
                # run created the file but failed to persist the path.
                if pres.get("thumbnail") != thumb_rel:
                    pres["thumbnail"] = thumb_rel
                skipped += 1
                continue

            if extract_first_page(pdf_path, out_png):
                print(f"ok  : week {wk} {pres['presenter']} -> {out_png.relative_to(ROOT)}")
                pres["thumbnail"] = thumb_rel
                generated += 1
            else:
                warnings += 1

    # Persist any thumbnail field updates back to weeks.yml
    with DATA_FILE.open("w") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, width=1000)

    print(f"\ndone. generated={generated} skipped={skipped} warnings={warnings}")
    return 0 if warnings == 0 else 0  # non-fatal


if __name__ == "__main__":
    sys.exit(main())
