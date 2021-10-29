#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#
'''
3
2 3 1

2
3
1
'''
def permutationEquation(p):
    # Write your code here
    # 找出每個1, 2, 3對應的x 1=p(3), 2=p(1), 3=p(2)
    res = [x+1 for i in range(1, len(p)+1) for x, v in enumerate(p)  if i == v]
    # 找出x對應的y 3=p(2), 1=p(3), 2=p(1)
    ans = [x+1 for i in res for x, v in enumerate(p) if i == v]
    
    return ans


def permutationEquation2(p):
    # 利用list.index找出索引值
    # 因為index是0->n-1，所以內層 p.index(i+1)
    # 找到索引值後，p.index也是0->n-1，所以要再+1 p.index(i+1)+1
    # 當找到1->n的x順序後，再用x找p(y)，也一樣要加1，p.index(p.index(i+1)+1)+1
    ans = [p.index(p.index(i+1)+1)+1 for i in range(n)]
    
    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
