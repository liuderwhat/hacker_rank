import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#
'''
5
47

thirteen minutes to six
'''
def minName(number) :

   if number == 1 : return "one"
   if number == 2 : return "two"
   if number == 3 : return "three"
   if number == 4 : return "four"
   if number == 5 : return "five"
   if number == 6 : return "six"
   if number == 7 : return "seven"
   if number == 8 : return "eight"
   if number == 9 : return "nine"
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"
   if number == 13 : return "thirteen"
   if number == 14 : return "fourteen"
   if number == 15 : return "quarter after"
   if number == 16 : return "sixteen"
   if number == 17 : return "seventeen"
   if number == 18 : return "eighteen"
   if number == 19 : return "nineteen"
   if number == 20 : return "twenty"
   if number == 21 : return "twenty one"
   if number == 22 : return "twenty two"
   if number == 23 : return "twenty three"
   if number == 24 : return "twenty four"
   if number == 25 : return "twenty five"
   if number == 26 : return "twenty six"
   if number == 27 : return "twenty seven"
   if number == 28 : return "twenty eight"
   if number == 29 : return "twenty nine"
   if number == 30 : return "thirty"
   return ""
def hourName(number) :
   if number == 1 : return "one"
   if number == 2 : return "two"
   if number == 3 : return "three"
   if number == 4 : return "four"
   if number == 5 : return "five"
   if number == 6 : return "six"
   if number == 7 : return "seven"
   if number == 8 : return "eight"
   if number == 9 : return "nine"
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"

def timeInWords(h, m):
    # Write your code here
    if m == 00:
            return '{} o\' clock'.format(hourName(h))
    elif m <= 30:
        if m % 15:
            if m == 1:
                return 'one minute past {}'.format(hourName(h))
            else:
                return '{0} minutes past {1}'.format(minName(m), hourName(h))
        elif m == 15:
            return 'quarter past {}'.format(hourName(h))
        elif m == 30:
            return 'half past {}'.format(hourName(h))
    elif m > 30:
        if m % 15:
            return '{0} minutes to {1}'.format(minName(60-m), hourName(h+1))
        else:
            return 'quarter to {}'.format(hourName(h+1))
if __name__ == '__main__':

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)
    print(result)

