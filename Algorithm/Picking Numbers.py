#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
# absolute difference between any two elements is less than or equal to 1
from itertools import product
def pickingNumbers(a):


    a_tmp = sorted(list(set(a)))
    pick = []
    pick_sum = []
    for i in range(len(a_tmp)):
        if i <= len(a_tmp)-2:
            if a_tmp[i+1]-a_tmp[i] == 1:
                pick.append(a_tmp[i])

    for i in a_tmp:
        if i in pick:
            pick_sum.append(a.count(i)+(a.count(i+1)))
        else:
            pick_sum.append(a.count(i))
def pickingNumbers3(a):


    l = sorted(list(set(a)))
    maximum=0
    for i in l:
        c=a.count(i)
        d=a.count(i-1)
        c=c+d
        if c > maximum:
            maximum=c
    return maximum
    
def pickingNumbers2(l):
    maximum=0
    for i in l:
        c=l.count(i)
        d=l.count(i-1)
        c=c+d
        if c > maximum:
            maximum=c
    return maximum

def pickingNumbers4(a):
    
    ans = []
    for i in a:

        tmp = [True for x in a if x-i==0 or x-i ==1]
        ans.append(sum(tmp))

    print(max(ans))

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers3(a)

    print(result)
