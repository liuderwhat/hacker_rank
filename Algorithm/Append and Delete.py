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

    for ops_left in range(k, 1, -1):

        if s == t[:len(s)] and len(t) - len(s) == ops_left or len(s) == 0:
            break
        s = s[:-1]
        print(ops_left)
    return"Yes" if len(t) - len(s) <= ops_left else "No"

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input().strip())

    result = appendAndDelete(s, t, k)

    print(result)