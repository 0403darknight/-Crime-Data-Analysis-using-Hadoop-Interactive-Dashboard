#!/usr/bin/env python3
import sys

current_state = None
total = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        state, value = line.split("\t", 1)
        value = float(value)
    except ValueError:
        continue

    if state == current_state:
        total += value
    else:
        if current_state is not None:
            print(f"{current_state},{total:g}")
        current_state = state
        total = value

if current_state is not None:
    print(f"{current_state},{total:g}")
