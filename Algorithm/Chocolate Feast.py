#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#
'''
3
10 2 5
12 4 4
6 2 2
'''
def chocolateFeast(n, c, m):
    # Write your code here
    # 先計算可以換幾個巧克力
    num_c = n // c
    count = 0
    # 當不能再用包裝紙換就停止
    while num_c >= m:
        # 計算可以用幫包裝紙換幾個
        wrap = num_c // m
        # 扣掉換得(剩餘的部分)
        surpass = num_c - wrap * m
        # 因為剩餘的部分也會當成下次的數量，
        # 而且剩餘的本來就是一開始有的，所以要扣掉
        count += num_c - surpass
        # 剩餘的+換的會是下次的總數
        num_c = wrap + surpass
    # 當還有完全換完就加起來
    if num_c > 0:
        count += num_c
    return count
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(result)
