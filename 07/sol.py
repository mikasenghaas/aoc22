#!/usr/bin/python3
import sys
import math
from collections import defaultdict

f = sys.argv[1] if len(sys.argv) > 1 else '7.in'
lines = [line.strip() for line in open(f).readlines()]

sizes = defaultdict(int)
paths = []
for line in lines:
    words = line.split(' ')
    if words[1] == 'cd':
        if words[2] == '..':
            paths.pop()
        else: 
            paths.append(words[2])
    elif words[1] == 'ls':
        continue
    else:
        if words[0] != 'dir':
            for i in range(len(paths)):
                sizes['/' + '/'.join(paths[1:i+1])] += int(words[0])

ans = 0
free = 30000000 - (70000000 - sizes['/'])
deletesize = math.inf
for k, v in sizes.items():
    if v >= free:
        deletesize = min(deletesize, v)
    if v <= 100000:
        ans += v
print(ans)
print(deletesize)
