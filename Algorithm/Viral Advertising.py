#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# there are five people initially

def viralAdvertising(n):
    count = 0
    people = 5
    # Write your code here
    for _ in range(n):
        liked = people // 2
        count += people // 2
        people = liked * 3
    return count

if __name__ == '__main__':

    n = int(input().strip())

    result = viralAdvertising(n)

    print(result)
