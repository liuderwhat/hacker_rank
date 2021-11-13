#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'surfaceArea' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY A as parameter.
#

'''
解釋:
有一個w*h的板子
板子上面的每一格都會有一個自己的高度
note: 每一格的面積是1*1
e.g. 

3 3

板子本人:
1 3 4
2 2 3
1 2 4

[0,0] -> 第[0,0]格的高度為1 
[0,1] -> 高度是3

問此情況的表面積是多少?

'''
def surfaceArea(A):

    # 計算最外圍的面積
    # 上下
    area = 2 * len(A[0]) * len(A)

    # 左右，因為是list，所以用zip把每一列的第一個跟最後一個相加
    fl_area = [i for i in zip(*A)]
    area += sum(fl_area[0]) + sum(fl_area[-1])

    # 前後，把第一列跟最後一列的數相加
    fb_area = sum(A[0])+sum(A[-1])

    area += fb_area
    

    # 計算重疊的部分

    # 分成左後跟前後 
    # 一列的左右要計算len(A[0])-1次
    # 整個矩陣的前後要計算len(A)-1次
    # 每次計算是一位置前後+左右

    # 因為每一列數子跑完: 左右比len(A[0])-1次
    # 但前後是比len(A[0])次，所以都要設條件避免超出範圍
    for i in range(1, len(A)+1):
         
        for x in range(1, len(A[0])+1):

            if x < len(A[0]):
                area += abs(A[i-1][x] - A[i-1][x-1])

            if i < len(A):
                area += abs(A[i][x-1] - A[i-1][x-1])
    return area

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    print(result)

'''
3 3
1 3 4
2 2 3
1 2 4
'''