#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy

    cost = p
    count = 0
    flag = True
    while(cost <= s):
        s -= cost
        count += 1

        if cost-d <= m and flag:
            cost=m
            flag = False
        elif cost-d > m:
            cost -= d
            
    return count





if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    print(answer)
