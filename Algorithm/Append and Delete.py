#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'appendAndDelete' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. STRING t
#  3. INTEGER k
#
'''
hackerhappy
hackerrank
9

yes
'''


def appendAndDelete(s, t, k):


    min_length = min(len(s), len(t))
    common = 0
    for i in range(min_length):

        if s[i] == t[i]:
            common+=1
        else:
            break

    # 刪減過的s + t刪去的部分 需要與原本的t相同

    diff = len(s) + len(t) - 2 * common

    # case1 
    # 因為是要拼裝，所以K一定大於等於diff
    if diff > k:
        return 'No'
    # case2
    # e.g. s = 01001; t=0100，diff是5+4-2*4=1，代表需要換1次
    # e.g. s = 01001; t=01001，diff是5+5-2*5=0，代表需要換0次
    elif diff % 2 == k % 2:
        return 'Yes'
    # case3
    # 要確定基偶不符合的情況
    elif (len(s) + len(t) - k) < 0:
        return 'Yes'
    # case4
    else:
        return 'No'



if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)