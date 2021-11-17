#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'strangeCounter' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER t as parameter.
#

def strangeCounter2(t):

    v = 3
    while(t > v):
            t -= v
            v *= 2
    return v-t+1

def strangeCounter(t):
    # Write your code here
    
    # 
    v = 3
    while(1):
        if t <= v:
            return v-t+1
        else:
            t -= v
            v *= 2

if __name__ == '__main__':

    t = int(input().strip())

    result = strangeCounter(t)

    print(result)
