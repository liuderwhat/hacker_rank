#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dayOfProgrammer' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER year as parameter.
#
'''
From 1700 to 1917, Russia's official calendar was the Julian calendar
 since 1919 they used the Gregorian calendar system. The transition from the Julian to Gregorian calendar system occurred in 1918
 
 it has 29 days during a leap year, and 28 days during all other years.
 
  In the Julian calendar, leap years are divisible by 4
  Divisible by 400. Divisible by 4 and not divisible by 100
'''
def dayOfProgrammer(year):
    # Write your code here
    
    # sum of days of month expect for February 
    month_day_total = 31 + 31 + 30 + 31 + 30 + 31 + 31
    # Gregorian
    if year > 1918:
        # leap year
        if (year %4 == 0 and year % 100 != 0) or year % 400 == 0:
             month_day_total += 29
        else : 
            month_day_total += 28
    # Julian
    elif year >= 1700 and year <= 1917:
        if year %4  == 0:
             month_day_total += 29
        else : 
            month_day_total += 28
    
    elif year == 1918:
        month_day_total += 28-14+1   
    res = 256 - month_day_total
    
    return '{}.{}.{}'.format(res, '09', year)
    
if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result)