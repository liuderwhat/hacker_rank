#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # 因為旋轉會有循環，所以先計算要轉幾次，不需要轉k次
    length_rotate = k % len(a)
    # 整個往右轉一次是l[-1]+l[:-1]，也就是最後面的放到最前面，然後第零個到倒數第二個放後面
    # 所以轉n次就是1換成n
    a_rotate = a[-length_rotate:] + a[:-length_rotate]

    return [a_rotate[i] for i in queries]

def circularArrayRotation(a, k, queries):

    k_cir = k%len(a)
    ans = [a[(k_cir*-1)+i] for i in range(len(a)) ]
    return [ans[i] for i in queries]
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)
    print(result)