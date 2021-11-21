#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoPluses' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY grid as parameter.
#
'''
5 6
GGGGGG
GBBBGB
GGGGGG
GGBBGB
GGGGGG

5
'''
'''
1. good ans index is uni
2. r, c size is same
'''
from functools import reduce

def twoPluses(grid):
    # Write your code here
    grid_l = list(grid)
    r = len(grid)
    c = len(grid[0])
    unit = list()
    unit_count_ud = 1
    unit_count_lr = 1
    pluss_ind = []
    pluss_all = []
    for i in range(r):
        

        for x in range(c):

            if grid_l[i][x] == 'G':
                print(i, x, sep=":")
                count = 1
                unit_count_ud = 1
                print('上下')

                while(i-count >= 0 and i+count <= r-1):

                    if grid_l[i-count][x] == grid_l[i+count][x]=='G':
                        unit_count_ud += 2
                        # print(((i+count, x),(i-count, x)))
                        pluss_ind.append([((i+count, x),(i-count, x))])
                        if i+count == r-1:
                            break
                        count+=1
                    else:
                        break
                count = 1
                print('左右')
                unit_count_lr = 1
                while(x-count >= 0 and x+count <= c-1 ):
                    if grid_l[i][x+count] == grid_l[i][x-count] == 'G' :
                        unit_count_lr += 2
                        # print(((i, x+count),(i, x-count)))
                        pluss_ind.append([((i, x+count),(i, x-count))])

                        if x+count == c-1:
                            break
                        count+=1
                    else:
                        break
            pluss_all.append(pluss_ind)
    print(pluss_all)
            # unit.append(min(unit_count_ud, unit_count_lr)*2-1)

    print(unit)
    return reduce(lambda x, y: x*y, unit)
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)

    print(result)