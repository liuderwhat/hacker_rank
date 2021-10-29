#!/bin/python3

import math
import os
import random
import re
import sys
'''
8 2
0 0 1 0 0 1 1 0

92
'''
# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    e = 100
    length = len(c)
    p = 0
    while(1): 
        p = (p+k)% length
        if c[p]:
            e -= 3
        else:
            e -= 1
        
        if p % length == 0:
            return e

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(result)
