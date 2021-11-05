import math
import os
import random
import re
import sys

from itertools import combinations
import timeit

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here

    all_com = list(combinations(topic, 2))
    ans = []
    for i in all_com:

        i = list(i)

        res = str(int(i[0])+int(i[1]))
        ans.append(sum([int(i)>0 for i in res]))

    return [max(ans), ans.count(max(ans))]

def acmTeam2(topic):

    # 用combinations找出所有組合，設定2表示兩兩一組
    all_com = list(combinations(topic, 2))
    # 紀錄每個組合的分數
    ans = []
    for i in all_com:
        # combinations的元素: set([str,str], ...)
        i = list(i)
        # 走訪整個list，若其中一個attendee有1就給True
        ans.append(sum([True for x in range(len(i[0])) if i[0][x]=='1' or i[1][x]=='1']))

    return [max(ans), ans.count(max(ans))]

def acmTeam3(topic):
    d = []
    resdic = {}
    m = 0
    # 找出每個attendee 1的位置
    for t in topic:
        temp = set()
        for i in range(len(t)):
            if t[i]=='1':
                temp.add(i)
        d.append(temp.copy())
    # 所有組合
    # 因為是紀錄位置，所以每個組合可用set的unoin紀錄有多少不一樣的
    for i in range(len(d)-1):
        for j in range(i+1,len(d)):
            l = len(d[i].union(d[j]))
            m = max(m,l)
            resdic[l]=resdic.get(l,0)+1
    return [m,resdic[m]]

if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    start = timeit.default_timer()
    result = acmTeam2(topic)
    stop = timeit.default_timer()

    start2 = timeit.default_timer()
    result = acmTeam3(topic)
    stop2 = timeit.default_timer()
    # print(*result, sep='\n')
    
    print(stop-start, stop2-start2, sep=" : ")