#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'workbook' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER_ARRAY arr
#
# 跟頁數一樣就是special
'''
5 3
4 2 6 1 10

4
'''

def workbook(n, k, arr):

    count = 0
    # 從第一頁開始
    page = 1

    for p in arr:
        p_arr = [i for i in range(1, p+1)]
        p_page = len(p_arr) // k
        surpass = len(p_arr) % k

        # 因為一頁也只會對上一個數字
        # 所以只要對上了就要換頁
        # 有翻頁的情況
        if p_page:
            for i in range(0, p_page):
                # 0-4, 5-9
                if page in p_arr[i*k:i*k+k]:
                    count +=1
                    # print(page, p, sep=":")
                page+=1
        # 剩下的頁數
        if surpass:
            if page in p_arr[-surpass:]:
                # print(page, p, sep=":")
                count +=1
            page+=1
    return count

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(result)

