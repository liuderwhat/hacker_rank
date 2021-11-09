#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'beautifulTriplets' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#

'''
7 3 
1 2 4 5 7 8 10 
'''
from itertools import combinations

def beautifulTriplets(d, arr):
    # Write your code here
    ans = 0
    for i in  combinations(arr, 3):
        if i[2]-i[1] == i[1]-i[0] == d:
            ans+=1

    return ans

def beautifulTriplets(d, arr):
    # Write your code here
    ans = 0
    # arr是map，所以先轉成list
    arr = list(arr)
    for i in range(len(arr)):
        # 用O(n)找每個數字+d跟+2*d是否在數列裡
        if arr[i]+d in arr and arr[i]+2*d in arr:

            ans+=1

    return ans

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = map(int, input().rstrip().split())

    result = beautifulTriplets(d, arr)

    print(result)
