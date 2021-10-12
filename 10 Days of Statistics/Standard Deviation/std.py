#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stdDev' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def stdDev(arr):
    # Print your answers to 1 decimal place within this function
    mean = sum(arr) / len(arr)
    squr_dis = [pow((i - mean), 2) for i in arr]
    print('{:.1f}'.format(math.sqrt((sum(squr_dis) / len(arr)))))
    
if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    stdDev(vals)
