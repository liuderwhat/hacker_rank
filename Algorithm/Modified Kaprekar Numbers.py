import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#
'''
1       p = 1
100     q = 100

1 9 45 55 99
'''
def kaprekarNumbers(p, q):
    # Write your code here
    d = 0
    ans = []
    for i in range(p, q+1):

        d = len(str(i))

        a, b = (i**2) // 10**d, (i**2) % 10**d

        if a+b == i:

            ans.append(str(i))
    if not len(ans):
        print('INVALID RANGE')
    else:
        print(' '.join(ans))
if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
