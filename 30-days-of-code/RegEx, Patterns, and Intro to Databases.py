import math
import os
import random
import re
import sys

'''
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

julia
julia
riya
samantha
tanya
'''

def f_name_order(firstName, emailID):

    # 匹配最後是@gmail.com的帳號
    pattern = '.*@gmail.com$'

    return re.match(pattern, emailID)



if __name__ == '__main__':
    N = int(input().strip())
    valid = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        if f_name_order(firstName, emailID):

            valid.append(firstName)
    valid.sort()

    [print(i) for i in valid]