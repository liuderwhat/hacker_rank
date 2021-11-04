#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

def taumBday(b, w, bc, wc, z):

    # 依題目分三種情況 哪個顏色比較貴或是一樣
    # 若有一個顏色比較貴的，就比較原本的方案與改顏色哪個貴
    if bc > wc:

        return wc * w + min(bc*b, wc*b+z*b)

    elif bc < wc:

        return bc * b + min(wc*w, bc*w+z*w)

    else:
        
        return bc*b +wc*w
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        print(result)
