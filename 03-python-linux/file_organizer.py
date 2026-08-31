#!/usr/bin/env python3
"""Organize files into folders by extension. Dry-run by default."""

import argparse
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".xls", ".xlsx", ".ppt", ".pptx"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Videos": {".mp4", ".mkv", ".avi", ".mov"},
    "Audio": {".mp3", ".wav", ".flac", ".m4a"},
    "Code": {".py", ".sh", ".js", ".ts", ".cpp", ".c", ".java"},
}


def category(path):
    suffix = path.suffix.lower()
    for name, extensions in CATEGORIES.items():
        if suffix in extensions:
            return name
    return "Others"


def main():
    parser = argparse.ArgumentParser(description="Organize a directory by file type")
    parser.add_argument("path", nargs="?", default="~/Downloads")
    parser.add_argument("--apply", action="store_true", help="actually move files")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"Not a directory: {root}")

    for path in root.iterdir():
        if not path.is_file():
            continue
        target = root / category(path) / path.name
        print(f"{path.name} -> {target.parent.name}/")
        if args.apply:
            target.parent.mkdir(exist_ok=True)
            shutil.move(str(path), str(target))

    if not args.apply:
        print("\nDry run only. Add --apply to move files.")


if __name__ == "__main__":
    main()
