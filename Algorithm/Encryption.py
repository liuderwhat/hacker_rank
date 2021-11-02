#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
'''
haveaniceday

hae and via ecy
'''
def encryption(s):
    # Write your code here

    length = len(s)
    row = math.floor(math.sqrt(length))
    col = math.ceil(math.sqrt(length))
    # 依照行列把字串切開 e.g. 123456 -> 123 456
    spilt_res = [s[(i)*col:(i+1)*col] for i in range(col)]
    # 因為長度不一定相等，所以計算長度
    res_leng = [len(i) for i in spilt_res]
    ans = []
    
    # 每一個迴圈會取每個spilt_res的當前的值
    for i in range(max(res_leng)):
        res = []
        # 判斷是否超過每個數列的長度，若無則加入
        for x in spilt_res:
            if len(x) >= i+1:
                res.append(x[i])
        ans.append(''.join(res))
        
    return (' '.join(ans))
def encryption2(s):
    # Write your code here

    length = len(s)
    row = math.floor(math.sqrt(length))
    col = math.ceil(math.sqrt(length))
    # 用類似slice的方式取出每一個index
    # list[st:ed:range]，代表從i開始到最後，每次會跳col個index，一個forloop會是一個答案
    return ' '.join([s[i::col] for i in range(col)])

if __name__ == '__main__':

    s = input()

    result = encryption2(s)

    print(result)