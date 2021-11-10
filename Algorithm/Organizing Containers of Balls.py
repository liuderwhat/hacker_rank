#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def organizingContainers(container):

    # 計算每個元素各有幾個
    ele_num = len(container[0])
    ele_count = [0]*ele_num
    for i in container:
        
        for index, v in enumerate(i):

            ele_count[index] += v

    # 算容器大小
    con_size = [sum(i) for i in container]
    ele_count.sort()
    con_size.sort()

    # 確保容器的大小均大於對應元素的數量
    # 因為交換次數不限，所以直接透過上述去判斷是否可能
    for i in range(len(ele_count)):
        if ele_count[i] > con_size[i]:
            return 'Impossible'
    else:
        return 'Possible'

if __name__ == '__main__':

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result)