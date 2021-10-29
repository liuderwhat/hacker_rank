import math
import os
import random
import re
import sys

'''
3
3 2 1

Array is sorted in 3 swaps.
First Element: 1
Last Element: 3
'''

def bubble(a):
    swap_count = 0
    tmp = 0
    for _ in range(len(a)):

        for i in range(len(a)-1):
            if a[i] > a[i+1]:

                tmp = a[i]
                a[i] = a[i+1]
                a[i+1] = tmp

                swap_count += 1

        if swap_count == 0:
            break
    print('Array is sorted in {} swaps.'.format(swap_count))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    bubble(a)
