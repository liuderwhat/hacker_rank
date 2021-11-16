#!/bin/python3

import math
import os
import random
import re
import sys

def bomberMan(n, grid, r, c):

    # 用set存一開始有炸彈的位置
    s = set()
    [s.add((i, x)) for i in range(r) for x in range(c) if grid[i][x] == 'O'] 
  
    # n為1代表沒動作
    # 建一個r*c大小，值為'.'的list
    # 把有炸彈的改為'O'
    if n == 1 :
        final = [['.' for i in range(c)] for j in range(r) ]
        for b in s:
            final[b[0]][b[1]] = 'O'

        return [''.join(i) for i in final]

    # 由規則推論，只要是偶數輪的所有位置都會被填滿炸彈
    # 所以直接傳r*c且值為'O'的list
    if not (n % 2):

        res = [['O' for i in range(c)] for x in range(r)]

    # 剩下是3與5的情況
    # 兩者都需要將被標記為炸彈的位置四周都改為'.'
    # 不一樣的是3的情況是做1次，5的情況做2次
    # 且也可推論出 3->7->11 會有相同答案
    #             5->9->14 會有相同答案
    # 可找出規則 (5-n%4)//2 是1或是2
    else:

        for _ in range((5-n%4)//2):

            final = [['O' for i in range(c)] for j in range(r) ]

            for b in s:

                # 上下左右的情況依序判斷

                final[b[0]][b[1]] = '.'

                if b[0] >= 1:
                    final[b[0]-1][b[1]] = '.'

                if b[0] <= r-2:
                    final[b[0]+1][b[1]] = '.'

                if b[1] >= 1:
                    final[b[0]][b[1]-1] = '.'

                if b[1] <= c-2:
                    final[b[0]][b[1]+1] = '.'

            # 當每一輪結束會重新標記炸彈位置
            s = set()
            [s.add((i, x)) for i in range(r) for x in range(c) if final[i][] == 'O']

    return final
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)
    result = bomberMan(n, grid, r, c)

    [print(''.join(i)) for i in result]