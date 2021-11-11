#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'serviceLane' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY cases
#
'''
8 5
2 3 1 2 3 2 3 3
0 3
4 6
6 7
3 5
0 7
'''
def serviceLane(n, cases, width):
    # Write your code here
    ans = []

    # 每個case會包含width的索引值
    # 找到索引值範圍的width，再取最小者
    for i in cases:

        wid = width[i[0]:i[1]+1]

        ans.append(min(wid))

    return ans

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases, width)

    print(result)
