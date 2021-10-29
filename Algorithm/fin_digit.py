#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def findDigits(n):
    # Write your code here
    str_n = str(n)
    c = 0
    for i in str_n:
        int_i = int(i)
        if int_i != 0 and n%int_i == 0:
            c+=1
    return c
def findDigits2(n):
    c = 0
    tmp = n
    while(tmp>0):
        res = tmp%10
        if res != 0 and n%res == 0:
            c += 1
        tmp = tmp // 10
    return c
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits2(n)

        print(result)