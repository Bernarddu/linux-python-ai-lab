#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-.}"

echo "Disk usage for: $TARGET"
echo "----------------------------------------"
du -h --max-depth=1 "$TARGET" 2>/dev/null | sort -h | tail -n 20

echo
echo "Filesystem usage:"
df -h "$TARGET"
