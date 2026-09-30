#!/usr/bin/env python3
import sys
import csv

reader = csv.DictReader(sys.stdin)

for row in reader:
    state = row.get("States/UTs", "").strip()
    value = row.get("Total Cognizable IPC crimes", "0").strip()

    if not state:
        continue

    try:
        value = float(value or 0)
    except ValueError:
        value = 0

    print(f"{state}\t{value:g}")
