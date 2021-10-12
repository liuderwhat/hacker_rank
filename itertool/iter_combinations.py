from itertools import combinations

'''
HACK 2

A
C
H
K
AC
AH
AK
CH
CK
HK
'''


def com_1(string, n):

    string, n = input().split()
    for i in range(1,int(n)+1):
        data = ["".join(sorted(i)) for i in combinations(string,i)]
        data.sort()
        print("\n".join(data))

def com_2(string, n):
    ans_list = []
    for i in range(1, int(n)+1):
        ans_list.append( list(combinations(string, i)) )

    for i in ans_list:
        ans_list_str = []
        for res in i:
            res = list(res)
            res.sort()
            ans_list_str.append(''.join(res))

        ans_list_str.sort()

        for i in ans_list_str: print(i)

string, n = input().strip().split()
com_1(string, n)
