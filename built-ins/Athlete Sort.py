'''
5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
'''

def ath_sort(ath_info, sort_att):
    s = sorted(ath_info, key = lambda x: x[sort_att])
    [print(*i) for i in s]

num_ath, num_att = list(int(num) for num in input().split())
ath_info = []
for _ in range(num_ath):
    ath_info.append(list(int(num) for num in input().split()))

sort_att = int(input())
ath_sort(ath_info, sort_att)

# list也可以不同長度
a = [[7,1, 0], [10, 2, 5, 0]]
s = sorted(a, key = lambda x: x[2]) # [[7, 1, 0], [10, 2, 5, 0]]