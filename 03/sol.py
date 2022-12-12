#!/usr/bin/python3
import sys 

f = sys.argv[1] if len(sys.argv) > 1 else "3.in"
lines = [line.strip() for line in open(f).readlines()]

vals = []
for line in lines: 
    n = int(len(line) / 2)
    a, b = line[:n], line[n:]
    common = list(set(a) & set(b))[0]
    val = ord(common) - 96 if ord(common) >= 0x61 else ord(common) - 38
    vals.append(val) 
print(sum(vals))

vals = []
for i in range(0, len(lines), 3):
    a, b, c =  lines[i], lines[i+1], lines[i+2]
    common = list(set(a) & set(b) & set(c))[0]
    val = ord(common) - 96 if ord(common) >= 0x61 else ord(common) - 38
    vals.append(val) 
print(sum(vals))
