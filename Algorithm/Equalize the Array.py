import math
import os
import random
import re
import sys

#
# Complete the 'equalizeArray' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
'''
5
3 3 2 1 3 
'''

def equalizeArray(arr):
    # 用set的特性找出唯一的元素
    set_arr = list(set(arr))
    # 用原來的list計算每個元素的出現次數
    count = [arr.count(i) for i in set_arr]
    # 因為是刪去多少個，所以算全部元素減最多的元素
    return len(arr) - max(count)

if __name__ == '__main__':

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    print(result)
