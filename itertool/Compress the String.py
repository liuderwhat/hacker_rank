'''
1222311
(1, 1) (3, 2) (1, 3) (2, 1)

'''
from itertools import groupby

def compress(string):

    res = [tuple( (len(list(g)), int(k)) ) for k, g in groupby(string)]
    
    print(*res)
string = input()
compress(string)