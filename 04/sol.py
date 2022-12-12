#!/usr/bin/python3
import sys

f = sys.argv[1] if len(sys.argv) > 1 else "4.in"
lines = [line.strip() for line in open(f).readlines()]

full_overlap = 0
any_overlap = 0
for line in lines:
    a,b = line.split(',')
    a1, a2 = map(int, a.split('-'))
    b1, b2 = map(int, b.split('-'))
    c = 0
    for i in range(a1, a2+1):
        if i >= b1 and i <= b2:
            c += 1
    if c == min(b2-b1+1, a2-a1+1):
        full_overlap += 1
    if c > 0:
        any_overlap += 1
print(full_overlap)
print(any_overlap)
