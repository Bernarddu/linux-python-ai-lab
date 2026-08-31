#!/usr/bin/env bash
set -euo pipefail

INTERVAL="${1:-2}"

echo "Process monitor — refresh every ${INTERVAL}s"
echo "Press Ctrl+C to exit."

while true; do
    clear
    echo "Linux Process Monitor — $(date '+%Y-%m-%d %H:%M:%S')"
    echo
    ps -eo pid,ppid,user,%cpu,%mem,stat,etime,comm --sort=-%cpu | head -n 16
    sleep "$INTERVAL"
done
