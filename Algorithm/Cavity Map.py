#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#
'''
4
1112
1912
1892
1234

1112
1X12
18X2
1234
'''
def cavityMap(grid):
    # Write your code here
    
    # 因為是square，所以取一邊的長度即可
    length = len(grid[0])

    # 因為本身是string，所以要用list處理
    # 也可以把全部轉成list直接做指派
    ans = []
    
    # 一列列檢查
    for r in range(length):
        res = []

        # 每一列的數字
        for c in range(length):

            # 忽略周圍的數字
            if c > 0 and r < length-1 and r > 0 and c < length-1:

                # 上下左右
                direction = list(map(int, [grid[r][c+1], grid[r+1][c], grid[r-1][c], grid[r][c-1]]))

                # 當大於周圍的，就符合條件
                if int(grid[r][c]) > max(direction):
                    res.append('X')
                else:
                    res.append(grid[r][c])
            else:
                res.append(grid[r][c])
        ans.append(''.join(res))

    return ans
if __name__ == '__main__':

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    print(result)
