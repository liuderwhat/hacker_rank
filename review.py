'''
haveaniceday
hae and via ecy
'''

import math
def encryption(l):

    length = len(l)

    row, col = math.floor(length**0.5), math.ceil(length**0.5)

    return ' '.join([l[i::col] for i in range(col)])
if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result)