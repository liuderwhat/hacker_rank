#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#  3 1 2 3 1 2 3
#  1 2 3 4 5 6 7 1 2 3 4 5 6

# 修改m以便可以正確循環 -> m - (n-s+1)
# 因為整除會是最後一個，所以加一個條件式判斷
def saveThePrisoner(n, m, s):
    # Write your code here
    res = (m - (n-s+1)) % n

    if res:
        return res
    else:
        return n

    return (s+m-2)%N+1
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        print(result)

