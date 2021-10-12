'''
HACK 2

AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

from itertools import permutations

def permu(string, n):
    
    res = [i for i in permutations(string, n)]
    res.sort()
    ans = [''.join(i) for i in res]
    [print(i) for i in ans]

string, n = input().strip().split()
permu(string, int(n))

