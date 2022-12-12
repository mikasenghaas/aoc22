#!/usr/bin/python3
import sys

f = sys.argv[1] if len(sys.argv) > 1 else "1.in"
lines = [line.strip() for line in open(f).readlines()]

s = 0
m = 0
elves = []
for line in lines:
    if not line:
        if s > m: 
            m = s
        elves.append(s)
        s=0
    else:
        s += int(line)
elves.append(s)

print(m)
print(sum(sorted(elves, reverse=True)[:3]))
