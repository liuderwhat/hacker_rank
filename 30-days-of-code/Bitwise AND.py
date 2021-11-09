#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bitwiseAnd' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER K
#
'''
1
8 5
STDIN
3
5 2
8 5
2 2
'''
def bitwiseAnd(N, K):
    # Write your code here
    max_num = 0
    for i in range(1, N+1):
        for x in range(i+1, N+1):

            val = i&x
            if val > max_num and val < K:
                max_num = val

    return max_num

# 最大且小於k的數字為k-1
# 
def bitwiseAnd2(N, K):

    # Write your code here

    return max(ans)
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        print(res)
