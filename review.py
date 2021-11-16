#!/bin/python3

import math
import os
import random
import re
import sys

def bomberMan(n, grid, r, c):

    s = set()

    [s.add((i, x)) for i in range(r) for x in range(c) if grid[i][x] == 'O'] 

    if n == 1 :
        final = [['.' for i in range(c)] for j in range(r) ]
        for b in s:

            final[b[0]][b[1]] = 'O'
        return [''.join(i) for i in final]

    if not (n % 2):

        res = [['O' for i in range(c)] for x in range(r)]

        
    else:

        for _ in range((5-n%4)//2):

            final = [['O' for i in range(c)] for j in range(r) ]

            for b in s:

                final[b[0]][b[1]] = '.'

                if b[0] >= 1:
                    final[b[0]-1][b[1]] = '.'

                if b[0] <= r-2:
                    final[b[0]+1][b[1]] = '.'

                if b[1] >= 1:
                    final[b[0]][b[1]-1] = '.'

                if b[1] <= c-2:
                    final[b[0]][b[1]+1] = '.'

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