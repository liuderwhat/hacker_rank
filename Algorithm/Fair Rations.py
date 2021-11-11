#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#
'''
5
2 3 4 5 6 

4
'''

def fairRations(B):
    # Write your code here

    count = 0

    # 先找出奇數
    odd = [i for i in range(len(B)) if B[i] %2]

    # 當奇數個數也是奇數就沒辦法轉成都偶數的
    if len(odd) % 2:
        return 'NO'

    # 用來跳過下一個index
    flag = True
    for i in range(len(odd)-1):

        # 兩個索引值間的差就是兩個數轉換的次數
        # 1 2 4 5 ---> 3 - 0 = 3
        # step 1 : 2 3 4 5
        # step 2 : 2 3 5 6
        # step 3 : 2 4 6 6
        if flag:
            count += (odd[i+1] - odd[i])
            flag = False
        else:
            flag = True

    return str(count*2)

if __name__ == '__main__':

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(result)