#!/usr/bin/env bash
set -euo pipefail

printf '%s\n' '========== Linux Health Check =========='

check() {
    local name="$1"
    local value="$2"
    printf '%-20s %s\n' "$name" "$value"
}

check "Hostname" "$(hostname)"
check "Uptime" "$(uptime -p)"
check "Load average" "$(cut -d' ' -f1-3 /proc/loadavg)"
check "Memory" "$(free -h | awk 'NR==2 {print $3 " / " $2}')"
check "Root disk" "$(df -h / | awk 'NR==2 {print $5 " used"}')"
check "Processes" "$(ps -e --no-headers | wc -l)"

if command -v systemctl >/dev/null 2>&1; then
    failed=$(systemctl --failed --no-legend 2>/dev/null | wc -l)
    check "Failed services" "$failed"
fi

if command -v ip >/dev/null 2>&1; then
    check "Network" "$(ip route get 1.1.1.1 2>/dev/null | head -1 || echo unavailable)"
fi

echo
echo "Health check completed."
