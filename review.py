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

6 6
BGBBGB
GGGGGG
BGBBGB
GGGGGG
BGBBGB
BGBBGB

-1 0 -1 -1 0 -1
 0 1  0  0 1  0
-1 0 -1 -1 0 -1
 0 1  0  0 1  0
-1 0 -1 -1 0 -1
-1 0 -1 -1 0 -1
'''

def twoPluses(grid):
    # Write your code here
    grid_l = [list(i) for i in grid]
    r = len(grid)
    c = len(grid[0])
    valid = list()
    ans = []
    for i in range(1, r-1):

        for x in range(1, c-1):
  
            if grid_l[i][x] == 'G':
                if grid_l[i-1][x] == grid_l[i+1][x] == grid_l[i][x+1] == grid_l[i][x-1] == 'G':

                    valid.append([i,x])
    
    for v in valid:
        print(v)
        vx, vy = v

        press_set = list()
        count = 1
        unit_count_ud = 0
        
        while(vx-count >= 0 and vx+count <= r-1):
            
            if grid_l[vx-count][vy] == grid_l[vx+count][vy]=='G':
                unit_count_ud += 2
                press_set.append([vx+count, vy])
                press_set.append([vx-count, vy])
                if vx+count == r-1:
                    break
                count+=1
            else:
                break
        count = 1
        unit_count_lr = 0
        while(vy-count >= 0 and vy+count <= c-1 and unit_count_lr < unit_count_ud):
            if grid_l[vx][vy+count] == grid_l[vx][vy-count] == 'G'  :
                unit_count_lr += 2
                press_set.append([vx, vy+count])
                press_set.append([vx, vy-count])
                if vy+count == c-1:
                    break
                count+=1
            else:
                break
        a = 0
        if unit_count_ud < unit_count_lr:
            press_set = press_set[:unit_count_ud]+ press_set[unit_count_ud:unit_count_ud*2]
        else:
            press_set = press_set[:unit_count_lr]+ press_set[-unit_count_lr:]
        
        press_set.append([vx, vy])
        a = len(press_set)
        # print(press_set)
        if len(valid) > 1:
            for v1 in valid:
                print(v1)
                b = list()
                unit_count_ud = 0
                unit_count_lr = 0
                v1x, v1y = v1

                if v1 != v:

                    if v1 not in press_set:
                        count = 1
                        
                        while(v1x-count >= 0 and v1x+count <= r-1):
                            
                            if grid_l[v1x-count][v1y] == grid_l[v1x+count][v1y]=='G':
                                
                                
                                if [v1x+count, v1y] in press_set or [v1x-count, v1y] in press_set:
                                    break
                                print((v1x+count, v1y), (v1x-count, v1y))
                                if v1x+count == r-1:
                                    unit_count_ud += 2
                                    break
                                unit_count_ud += 2
                                count+=1
                            else:
                                break
                        count = 1
                        
                        while(v1y-count >= 0 and v1y+count <= c-1 ):
                            if grid_l[v1x][v1y+count] == grid_l[v1x][v1y-count] == 'G' :
                                
                                if [v1x, v1y+count] in press_set or [v1x, v1y-count] in press_set:
                                    break
                                print((v1x, v1y+count), (v1x, v1y-count))
                                if v1y+count == c-1:
                                    unit_count_lr += 2
                                    break
                                unit_count_lr += 2
                                count+=1
                            else:
                                break

                        b.append(min(unit_count_ud, unit_count_lr))
                        print(a, max(b)*2+1, sep=":")
                        ans.append(a* (max(b)*2+1))
                    else:
                        ans.append(a)
            print('+'*10)

        else:
            return a
    if len(ans) >= 1:
        print(sorted(ans))
        return max(ans)
    else:
        return 1
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