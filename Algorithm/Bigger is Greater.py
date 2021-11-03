import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

'''
lexicographical
Condensed mathematical description:

Find largest index i such that array[i − 1] < array[i].
(If no such i exists, then this is already the last permutation.)

Find largest index j such that j ≥ i and array[j] > array[i − 1].

Swap array[j] and array[i − 1].

Reverse the suffix starting at array[i].
'''
def biggerIsGreater(w):
    
    # 用來存答案
    ans = []
    # tmp存i，tmp2存j
    tmp = -1
    tmp2 = -1
    # 因為string為immutable，所以轉成list讓內容可改變
    w = list(w)

    # 依照步驟1找到最大的i
    for i in range(1, len(w)):
        if(w[i] > w[i-1]):
            tmp = i

    # 當找不到也代表此數列為由大到小排序的
    # 因此不用做更動
    if tmp == -1:
        return 'no answer'

    # 依照步驟2找j
    for j in range(len(w)):

        if(w[j] > w[tmp-1] and j >= tmp):
            tmp2 = j

    # 更換w[i-1]跟w[j]
    tamp = w[tmp-1]
    w[tmp-1] = w[tmp2]
    w[tmp2] = tamp
    
    # 最後從i開始到最後的值做排序
    ans = w[:tmp] + sorted(w[tmp:])

    return ''.join(ans)

if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)