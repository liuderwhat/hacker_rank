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

    spilt_res = [s[(i)*col:(i+1)*col] for i in range(col)]
    res_leng = [len(i) for i in spilt_res]
    ans = []

    for i in range(max(res_leng)):
        res = []
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