#!/usr/bin/env bash
set -euo pipefail

echo "========================================"
echo "        Linux System Information"
echo "========================================"
echo

echo "Hostname : $(hostname)"
echo "User     : $(whoami)"
echo "Kernel   : $(uname -sr)"
echo "Uptime   : $(uptime -p)"
echo "Date     : $(date '+%Y-%m-%d %H:%M:%S')"
echo

echo "CPU      : $(nproc) logical cores"
if command -v free >/dev/null 2>&1; then
    free -h | awk 'NR==2 {print "Memory   : " $3 " / " $2}'
fi
if command -v df >/dev/null 2>&1; then
    df -h / | awk 'NR==2 {print "Disk /   : " $3 " / " $2 " (" $5 ")"}'
fi

echo
if command -v lsb_release >/dev/null 2>&1; then
    echo "OS       : $(lsb_release -ds)"
elif [ -f /etc/os-release ]; then
    . /etc/os-release
    echo "OS       : ${PRETTY_NAME:-Unknown}"
fi
