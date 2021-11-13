#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G, P):
    # Write your code here

    # row and col length
    r = len(P[0])
    c = len(P)

    # 紀錄P目前比到第幾列
    cur_p_row = 0

    '''
    比法: 先從第一列開始比
    假如一樣就換下一列
    假如cur_p_row已經是最後一列了且也相同就return 'Yes'
    ''' 
    for i_c in range(len(G)-c+1):
        for i_r in range(len(G[0])-r+1):
            temp = i_c
            while G[temp][i_r:i_r+r] == P[cur_p_row]:
                temp+=1
                if cur_p_row == c-1:
                    return 'YES'
                cur_p_row +=1
            cur_p_row = 0

    return 'NO'

if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        print(result)
