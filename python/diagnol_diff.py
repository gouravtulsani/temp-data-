#!/bin/python3

import sys


n = int(input())
a = []
sum1=0
sum2=0
for i in range(n):
	a_t = list(map(int, input().split(" ")))
	a.append(a_t)
	a_t=0


for i in range(n):
	sum1+=a[i][i]
	sum2+=a[i][n-i-1]

print(sum1,sum2)
print(abs(sum1-sum2))
    