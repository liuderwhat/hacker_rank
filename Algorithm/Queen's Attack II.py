#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#
'''
5 3
4 3
5 5
4 2
2 3

10
'''
def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    q_pos = [[r_q, c_q]]
    a_pos = []
    
    # 上下
    for i in range(n-r_q, 0, -1):
        a_pos.append([r_q+i, c_q])
    for i in range(1, r_q):
        a_pos.append([r_q-i, c_q])
    # 左右
    for i in range(n-c_q, 0, -1):
        a_pos.append([r_q, c_q+i])
    for i in range(1, c_q):
        a_pos.append([r_q, c_q-i])

    # 左上右下
    for i in range(1, n+1):
        if r_q+i > n or c_q-i<=0:
            break
        else:
            a_pos.append([r_q+i, c_q-i])

    for i in range(1, n+1):
        if r_q-i <= 0 or c_q+i>n:
            break
        else:
            a_pos.append([r_q-i, c_q+i])

    # 右上左下
    for i in range(1, n+1):
        if r_q+i > n or c_q+i>n:
            break
        else:
            a_pos.append([r_q+i, c_q+i])

    for i in range(1, n+1):
        if r_q-i <= 0 or c_q-i<=0:
            break
        else:
            a_pos.append([r_q-i, c_q-i])

    for i in obstacles:
        # 上下
        if i[0] < r_q and  i[1] == c_q:
            for x in range(i[1]):
                a_pos.remove([i[0]-x, i[1]])
        elif i[0] > r_q and  i[1] == c_q:
            for x in range(n-i[1]):
                a_pos.remove([i[0]+x, i[1]])
        # 左右
        elif i[1] < c_q and i[0] == r_q:
            for x in range(i[1]):
                a_pos.remove([i[0], i[1]-x])
        elif i[1] > c_q and i[0] == r_q:
            for x in range(i[1]):
                a_pos.remove([i[0], i[1]+x])

    return a_pos
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    print(result)
