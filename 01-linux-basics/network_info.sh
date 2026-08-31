#!/usr/bin/env bash
set -euo pipefail

echo "========================================"
echo "          Linux Network Info"
echo "========================================"
echo

if command -v ip >/dev/null 2>&1; then
    echo "Interfaces:"
    ip -brief addr
    echo
    echo "Default route:"
    ip route | grep '^default' || echo "No default route found"
else
    echo "The 'ip' command is not available."
fi

echo
echo "DNS configuration:"
if [ -f /etc/resolv.conf ]; then
    grep -E '^(nameserver|search)' /etc/resolv.conf || true
fi
