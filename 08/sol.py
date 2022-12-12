#!/usr/bin/python3
import sys

f = sys.argv[1] if len(sys.argv) > 1 else "8.in"
T = [[int(c) for c in line.strip()] for line in open(f).readlines()]
n = len(T)

t = 2*n+2*(n-2)
ms = 0
for i in range(1, n-1):
    for j in range(1, n-1):
        el = T[i][j]
        top, bottom, left, right = True, True, True, True
        s1, s2, s3, s4 = 0, 0, 0, 0
        # look top
        for ii in range(i-1, -1, -1):
            s1 += 1
            if T[ii][j] >= el:
                top = False
                break
        for ii in range(i+1, n):
            s2 += 1
            if T[ii][j] >= el:
                bottom = False
                break
        for jj in range(j-1, -1, -1):
            s3 += 1
            if T[i][jj] >= el:
                left = False
                break
        for jj in range(j+1, n):
            s4 += 1
            if T[i][jj] >= el:
                right = False
                break

        s = s1 * s2 * s3 * s4
        ms = max(ms, s)

        if top or bottom or left or right:
            t += 1
print(t)
print(ms)
