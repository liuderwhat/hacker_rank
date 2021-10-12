#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#
def find_dis(string):
    a = set()
    b = set()
    for i in string:
        if i not in a:
            a.add(i)
        else:
            b.add(i)
    return list(b)

def checkMS(s):

    sum_s = sum(s[0])
    for i in s:
        if sum(i) != sum_s:
            return False

    zip_s = zip(*s)
    for i in zip_s:
        if sum(i) != sum_s:
            return False
    
    diag = 0
    diag_1 = []
    diag_2 = []
    for i in s:
        diag_1.append(i[len(i)-diag-1])
        diag_2.append(i[diag])
        diag+=1

    if sum(diag_1) != sum_s or sum(diag_2) != sum_s:
        return False
    
    return True
def formingMagicSquare(s):
    # Write your code here
    x = []
    for i in s:
        x.extend(i)
    repeat_num = find_dis(x)
    
    none_num = [i for i in range(1,10) if i not in x]
    
    
    
if __name__ == '__main__':
    
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
