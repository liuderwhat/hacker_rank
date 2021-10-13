#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#

def pageCount(n, p):
    # Write your code here
    l_count = 1
    u_count = 0
    u_first_page = 0
    if p == 1 or p ==n:
        return 0

    for i in range(2,n+1,2):
        if i == p or i+1 == p:
            break
        else:
            l_count += 1
    if n % 2 :
        if p ==n or p == n-1:
            return 0
        else:
            u_first_page = 2
            u_count = 1
    else:
        u_first_page = 1
        u_count = 1

    for i in range(n-u_first_page, -1, -2):
        if i == p or i-1 == p:
            break
        else:
            u_count += 1

    return min([u_count, l_count])

def pageCount2(n, p):

    # 每頁與第一頁的距離為 x // 2，因為每次都會翻兩頁，所以p//2可算出目標與第一頁的距離
    # n//2 - p//2 為最後一頁到目標頁數的距離
    return min(p//2, n//2 - p//2)

if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)