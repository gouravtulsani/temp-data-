#!/bin/python3

import sys

arr = list(map(int, input().split(' ')))
minar = []
maxar = []
maxx=0
minx=0
for i in range(4):
    maxar.append(max(arr))
    maxx += max(arr)
    arr.remove(max(arr))
for i in maxar:
    arr.append(i)
    
for i in range(4):
    minar.append(min(arr))
    minx += min(arr)
    arr.remove(min(arr))

print(maxx, minx)