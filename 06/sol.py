#!/usr/bin/python3
import sys

f = sys.argv[1] if len(sys.argv) > 1 else '6.in'
lines = [line.strip() for line in open(f).readlines()]

msg = lines[0]

for i in range(4, len(msg)):
    chars = set(msg[i-4: i])
    if len(chars) == 4:
        break
for j in range(14, len(msg)):
    chars = set(msg[j-14: j])
    if len(chars) == 14:
        break
print(i)
print(j)
