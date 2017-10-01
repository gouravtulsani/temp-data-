#!/bin/python3
#arr = [33,73,38,67,49,25,93]

import sys
i = 68
if i >= 38:
    if i%10>=8:
        i += (10-(i%10))
    elif i%5>=3:
        i += (5-(i%5))

print(i)