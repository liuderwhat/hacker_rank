#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'squares' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#
'''
2
3 9
17 24

2
0
'''
def squares(a, b):
    # Write your code here
    c = 0
    s = 1
    while(1):

        if pow(s, 2) >= a and pow(s, 2) <= b :
            c+=1

        if pow(s, 2) > b:
            return c

        s+=1

def squares2(a, b):
    # c = 0
    # for i in range(a, b+1):

    #     if  math.sqrt(i).is_integer():
    #         c += 1

    # return c
    return sum([True for i in range(a, b+1) if math.sqrt(i).is_integer()])

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        print(result)

