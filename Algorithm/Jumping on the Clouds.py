#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#
'''
6
0 0 0 1 0 0
'''
def jumpingOnClouds(c):
    # Write your code here
    step = 0
    continue_again = False
    
    # 因為不能中途改變range()的參數
    # 所以當遇到1用兩個continue代替...
    for i in range(len(c)):

        if continue_again:
            continue_again = False
            continue
        # 確定不超過長度
        if i+2 < len(c):
            # 當下一個是0就continue
            if c[i+2] == 0:
                step+=1
                continue_again = True
                continue
            else:
                step+=1
        # 假如跳的那格是最後一個就結束，但也要加一步
        elif i+2 == len(c):
            return step+1

    return step

def jumpingOnClouds2(c):

    i = 0
    step = 0
    while(i<=len(c)-1):
        if i+2 < len(c)-1:

            if c[i+2] ==0:
                step+=1
                i+=2
            else:
                step+=1
                i+=1
        elif i+2 > len(c)-1:
            return step+1
        elif i+2 == len(c)-1:
            return step+1

    return step



if __name__ == '__main__':

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds2(c)

    print(result)