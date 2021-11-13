#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    # Write your code here
    n_list = [i for i in range(1, n+1)]

    # 當N是奇數且k不是0則無法交換
    if not n % 2:

        # 不動
        if k == 0:
            return n_list

        # 當k*2可被整除則可用每k*2個去交換
        if not n % (k * 2) :

            # 每k*2個交換一次
            for i in range(0, n-1, k*2):

                # 看k是多少去交換k*2個
                # 若k = 1 則交換2個 1234-> [21][43]，先換12再換34
                # 若k = 2 則交換4個 1234 -> [3412] 一次34跟12
                t = n_list[i:i+k]
                n_list[i:i+k] = n_list[i+k:i+2*k]
                n_list[i+k:i+2*k] = t

            return n_list
        else:
            return [-1]
    else: 
        if k == 0:
            return n_list
        else:
            return [-1]

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        print(result)

'''
10
10 0
10 1
7 0
10 9
9 0
10 3
8 2
8 0
7 0
10 1
'''