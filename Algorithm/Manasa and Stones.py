#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#

def stones2(n, a, b):
    # Write your code here
    # conse diff is a or b

    # 直接找所有情況的組合，然後很慢
    a = {sum(i) for i in product([a, b], repeat=n-1)}

    return sorted(list(a))

def stones(n, a, b):

    # 因為可以知道石頭的最大與最小
    # 所以以此兩數當成初始跟結束
    min_n = min(a, b)
    max_n = max(a, b)
    current = min_n * (n-1)
    max_stone = max_n * (n-1)
    
    # 計算不同情況
    # e.g. 10+10+10=30 (a, a, a)
    # 下一個假設是100-10(b-a) -> 30 +200
    # 也可以表示 a + a + a + b -a = a a b ，以此類推直到加到最大值
    diff = max_n - min_n
    
    if min_n == max_n:
        return current
    else:
        ans = []

        while(current <= max_stone):

            ans.append(current)
            current += diff

        return ans
if __name__ == '__main__':

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        print(result)
