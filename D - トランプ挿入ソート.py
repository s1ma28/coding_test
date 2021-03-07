#!/usr/bin/env python3
# *coding: utf-8

from bisect import bisect_left

N = int(input())
C = [int(input()) for _ in range(N)]
L = []
for c in C:
    p = bisect_left(L, c)
    if p < len(L):
        L[p] = c
    else:
        L.append(c)
print(N-len(L))
