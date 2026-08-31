#!/usr/bin/env python3
"""Small cross-platform-ish Linux system monitor using only the standard library."""

import os
import shutil
import time
from datetime import datetime


def read_cpu_times():
    with open("/proc/stat", "r", encoding="utf-8") as f:
        fields = f.readline().split()[1:]
    values = list(map(int, fields))
    idle = values[3] + (values[4] if len(values) > 4 else 0)
    total = sum(values)
    return total, idle


def cpu_percent(previous):
    current = read_cpu_times()
    total_delta = current[0] - previous[0]
    idle_delta = current[1] - previous[1]
    if total_delta <= 0:
        return 0.0
    return 100.0 * (1 - idle_delta / total_delta)


def memory_percent():
    mem = {}
    with open("/proc/meminfo", "r", encoding="utf-8") as f:
        for line in f:
            key, value = line.split(":", 1)
            mem[key] = int(value.strip().split()[0])
    total = mem["MemTotal"]
    available = mem.get("MemAvailable", mem["MemFree"])
    return 100.0 * (total - available) / total


def main():
    previous = read_cpu_times()
    while True:
        time.sleep(1)
        cpu = cpu_percent(previous)
        previous = read_cpu_times()
        mem = memory_percent()
        disk = shutil.disk_usage("/")
        disk_pct = disk.used / disk.total * 100

        os.system("clear")
        print("Linux Python System Monitor")
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("-" * 40)
        print(f"CPU     : {cpu:6.2f}%")
        print(f"Memory  : {mem:6.2f}%")
        print(f"Disk /  : {disk_pct:6.2f}%")
        print(f"Cores   : {os.cpu_count()}")
        print("\nPress Ctrl+C to exit.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nMonitor stopped.")
