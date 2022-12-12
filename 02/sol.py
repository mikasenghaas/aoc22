#!/usr/bin/python3
import sys

f = sys.argv[1] if len(sys.argv) > 1 else "2.in"
lines = [line.strip() for line in open(f).readlines()]

points1 = {'AX': 4, 'BX': 1, 'CX':7,
           'AY': 8, 'BY': 5, 'CY':2,
           'AZ': 3, 'BZ': 9, 'CZ':6}

points2 = {'AX': 3, 'BX': 1, 'CX':2,
           'AY': 4, 'BY': 5, 'CY':6,
           'AZ': 8, 'BZ': 9, 'CZ':7}


t1, t2 = 0, 0
for line in lines:
    o = line.replace(' ', '')
    t1 += points1[o]
    t2 += points2[o]
print(t1)
print(t2)
