'''
HACK 2

AA
AC
AH
AK
CC
CH
CK
HH
HK
KK
'''
from itertools import combinations_with_replacement as cwr

def com_with_replace(string, n):

    res = [''.join(sorted(x)) for x in cwr(string, n)]
    res.sort()
    [print(i) for i in res]

string, n = input().strip().split()

com_with_replace(string, int(n))