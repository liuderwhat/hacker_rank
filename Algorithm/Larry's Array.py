#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'larrysArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY A as parameter.
#
'''
      A           rotate (rotate from any index)
[1,6,5,2,4,3]    [6,5,2]
[1,5,2,6,4,3]    [5,2,6]
[1,2,6,5,4,3]    [5,4,3]
[1,2,6,3,5,4]    [6,3,5]
[1,2,3,5,6,4]    [5,6,4]
[1,2,3,4,5,6]

YES

Choose any 3 consecutive indices and rotate their elements
'''

def larrysArray(A):
    parirty = 0
    
    for i, v in enumerate(A):
        
        parirty += sum([x < v for x in A[i:]])
        
    if parirty % 2:
        return "NO"
    else:
        return "YES"
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        print(results)
