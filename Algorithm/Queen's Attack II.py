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
        if i in a_pos:
            # D
            if i[0] < r_q and  i[1] == c_q:
                for x in range(i[0]):
                    if [i[0]-x, i[1]] in a_pos:
                        a_pos.remove([i[0]-x, i[1]])
            # U
            elif i[0] > r_q and  i[1] == c_q:
                for x in range(n-i[0]+1):
                    if [i[0]+x, i[1]] in a_pos:
                        a_pos.remove([i[0]+x, i[1]])
            # L
            elif i[1] < c_q and i[0] == r_q:
                for x in range(i[1]):
                    if [i[0], i[1]-x] in a_pos:
                        a_pos.remove([i[0], i[1]-x])
            # R
            elif i[1] > c_q and i[0] == r_q:
                for x in range(n-i[1]+1):
                    if [i[0], i[1]+x] in a_pos:
                        a_pos.remove([i[0], i[1]+x])
            # RU
            elif i[1] > c_q and i[0] > r_q:
                # RU-R
                if i[0] >= i[1]:
                    for x in range(n-i[0]+1):
                        if [i[0]+x, i[1]+x] in a_pos:
                            a_pos.remove([i[0]+x, i[1]+x])
                # RU-L
                else:
                    for x in range(n-i[1]+1):
                        if [i[0]+x, i[1]+x] in a_pos:
                            a_pos.remove([i[0]+x, i[1]+x])
            # LD
            elif i[1] < c_q and i[0] < r_q:
                if i[0] <= i[1]:
                    for x in range(i[0]):
                        if [i[0]-x, i[1]-x] in a_pos:
                            a_pos.remove([i[0]-x, i[1]-x])
                else:
                    for x in range(i[1]):
                        if [i[0]-x, i[1]-x] in a_pos:
                            a_pos.remove([i[0]-x, i[1]-x])

            # RD
            elif i[1] > c_q and i[0] < r_q:
                if i[0] <= n-i[1]:
                    for x in range(n-i[0]+1):
                        if [i[0]-x, i[1]+x] in a_pos:
                            a_pos.remove([i[0]-x, i[1]+x])
                else:
                    for x in range(n-i[1]+1):
                        if [i[0]-x, i[1]+x] in a_pos:
                            a_pos.remove([i[0]-x, i[1]+x])
            # LU
            elif i[1] < c_q and i[0] > r_q:
                if n-i[0] <= i[1]:
                    for x in range(n-i[0]+1):
                        if [i[0]+x, i[1]-x] in a_pos:
                            a_pos.remove([i[0]+x, i[1]-x])
                else:
                    for x in range(n-i[1]+1):
                        if [i[0]+x, i[1]-x] in a_pos:
                            a_pos.remove([i[0]+x, i[1]-x])
    return len(a_pos)
def display(result, n, r_q, c_q):

    for x in range(n, 0, -1):

        for i in range(1, n+1):

            if [x, i] in result:
                print(u"\u2591", end=' ')
            else:
                if [x, i] == [r_q, c_q]:
                    print("Q", end=' ')
                else:
                    print(u"\u2593", end=' ')
        else:
            print()


def queensAttack(n, k, r_q, c_q, obstacles):

    # 用set comprehension 因為set與dict的存取速度O(1)比list快O(n)
    obst = {(ob[0],ob[1]) for ob in obstacles}

    # 8個方向
    direction = [(1, 0), (-1, 0), (0, -1),(0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    count = 0
    
    # 每次往一個方向加，碰到障礙就停止
    for m in direction:
        r, c = r_q, c_q
        while((r+m[0] <= n and r+m[0]>=1) and (c+m[1] <= n and c+m[1] >= 1)):
            r += m[0]
            c += m[1]

            if (r, c) in obst:
                break
            else:
                count += 1
    return count
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

    # display(result, n, r_q, c_q)
    print(result)
