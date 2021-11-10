import math
import os
import random
import re
import sys

#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

# 將不一樣的部分反轉
def reverse(arr, s, t):
    a = arr[s:t+1]
    a.reverse()
    arr = arr[:s] + a + arr[t+1:]
    return arr

# 檢查索引值是否為連續的
def checkCon(diff, arr):
    for i in range(len(diff)-1):
        # 當不連續時，檢查缺失的值是否為中間數
        # 因為是與已排序的數列比較
        # 所以中間值可能會一樣
        if diff[i+1]-diff[i] != 1:
            # 中間值
            mid_diff = arr[diff[len(diff)//2]-1]
            # 中間值的索引值
            mid_index = diff[len(diff)//2]-1
            # 若不在則為特殊裝況
            # 需要插入diff裡
            if mid_index not in diff:
                diff.insert(len(diff)//2, mid_index)
            else:
                return False
    return True

def almostSorted(arr):
    # Write your code here
    ans_arr = sorted(arr)
    if arr == ans_arr:
        return 'yes'
    else:
        diff = [i for i in range(len(arr)) if arr[i] != ans_arr[i]]
        # 若只有兩個則一定可以
        if len(diff) == 2:
            print('yes')
            print('swap {0} {1}'.format(diff[0]+1, diff[1]+1))
        else:
            if checkCon(diff, arr):
                # 反轉不一樣的區間
                if reverse(arr, diff[0], diff[-1]) == ans_arr:
                    print('yes')
                    print('reverse {0} {1}'.format(diff[0]+1, diff[-1]+1))
                else:
                    print('no')
            else:
                print('no')
#############################################################################
def is_sorted(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

def almostSorted2(arr):
    if is_sorted(arr): 
        print('yes')
        return
    
    # iterate through the array and find the first and last unsorted element
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            break
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] < arr[j-1]:
            break
            
    # swap them and check if sorted
    if is_sorted(swap(arr[:], i, j)):
        print('yes')
        print('swap {} {}'.format(i+1, j+1))
        return
    
    # reverse section of array and check if sorted
    for k in range(i, math.ceil((j+i)/2), 1):
        arr = swap(arr, k, i + j - k)
        
    if is_sorted(arr):
        print('yes')
        print('reverse {} {}'.format(i+1, j+1))
        return
                
    print('no')
if __name__ == '__main__':
    f = open('almost_sorted.txt', 'r')

    first_line = f.readline()
    second_line = f.readline()

    arr = list(map(int, second_line.split(' ')))

    # n = int(input().strip())

    # arr = list(map(int, input().rstrip().split()))
    almostSorted(arr)
    # almostSorted2(arr)
