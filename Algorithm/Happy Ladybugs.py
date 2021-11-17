#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#
'''
5
5
AABBC
7
AABBC_C
1
_
10
DD__FQ_QQF
6
AABCBC

NO
YES
YES
YES
NO
'''

def happy(b):
    for a in set(b):
        if a != "_" and b.count(a) == 1:
            return "NO"
    
    if b.count("_") == 0:
        for i in range(1,n-1):
            if b[i-1]!=b[i] and b[i+1]!=b[i]:
                return "NO"
    return "YES"

def happyLadybugs(b):
    # Write your code here
    uni = set()
    repeat = set()
    flag = True
    for i in b:
        if i in uni:
            repeat.add(i)
        else:
            uni.add(i)
    print(uni.difference(repeat))
    if len(uni.difference(repeat)) == 1:
        if '_' not in uni.difference(repeat):
            return 'NO'
        else:
            return 'YES'
    elif len(uni.difference(repeat)) > 1:
        return 'NO'
    elif len(uni.difference(repeat)) == 0 and '_' in b:
        return 'YES'
    elif len(uni.difference(repeat)) == 0 and '_' not in b:

        for i in range(len(b)-1):
            
            if (not flag) and b[i] != b[i+1]:
                return 'NO'

            if b[i] == b[i+1]:
                flag = True
            else:
                flag = False
        return 'YES'
    else:
        print(123)
        return 'YES'
if __name__ == '__main__':

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        print(result)
