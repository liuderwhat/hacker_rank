#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.

'''
5 2
0 4

2
'''
def flatlandSpaceStations2(n, c):


    max_n = 0

    for i in range(n):
        # 找出非station的索引值，然後跟每個station的索引值相減
        if i not in c:
            spa_dis = []
            spa_dis = [abs(i-x) for x in c]

            if max_n < min(spa_dis):
                max_n = min(spa_dis)
    return max_n

def flatlandSpaceStations(n, c):

    c.sort()
    # 因為可能出現station後面或前面都沒station的情況
    # 造成實際答案比station間還大
    # 此兩種情況取最大值
    max_n = max(c[0], n-1-c[-1])

    # 計算每個station間的距離，因為是此點與個別的距離
    # 所以利用"dis // 2"算出實際的距離
    for i in range(len(c)-1):
        max_n = max(max_n, (c[i+1]-c[i]) // 2)

    return max_n
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(result)