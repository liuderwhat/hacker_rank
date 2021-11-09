#!/bin/python3

import math
import os
import random
import re
import sys
import timeit

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
'''
6
7 1 3 4 1 7
'''
def minimumDistances(a):
    # Write your code here

    # 找出有重複出現的字
    same = [i for i in a if a.count(i)>1]
    same = set(same)
    ans = []

    # 找出每個字的索引值再互減
    for i in same:
        res = [x for x in range(len(a)) if a[x] == i]
        ans.append(abs(res[0]-res[1]))

    if len(ans) > 0:
        return min(ans)
    else:
        return -1

def minimumDistances2(a):

    d = {}
    min_d = len(a)
    for i in range(len(a)):

        try:
            min_d = min(i-d[a[i]], min_d)
            d[a[i]] = i
            if min_d == 1:
                break
        except:
            d[a[i]] = i

    if min_d == len(a):
        return -1
    else:
        return min_d
if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))


    # result = minimumDistances2(a)

    start = timeit.default_timer()
    result = minimumDistances(a)
    stop = timeit.default_timer()

    start2 = timeit.default_timer()
    result = minimumDistances2(a)
    stop2 = timeit.default_timer()
    # print(*result, sep='\n')
    
    print(stop-start, stop2-start2, sep=" : ")
    # 0.02416080000000065 : 0.0006152000000021474