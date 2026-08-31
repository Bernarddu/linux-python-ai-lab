#!/usr/bin/env python3
"""Show the largest files under a directory."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description="Find large files")
    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-n", type=int, default=20, help="number of files to show")
    args = parser.parse_args()

    root = Path(args.path).expanduser().resolve()
    files = []
    for path in root.rglob("*"):
        try:
            if path.is_file():
                files.append((path.stat().st_size, path))
        except (OSError, PermissionError):
            continue

    print(f"Largest files under {root}\n")
    for size, path in sorted(files, reverse=True)[: args.n]:
        print(f"{size / 1024 / 1024:10.2f} MB  {path}")


if __name__ == "__main__":
    main()
