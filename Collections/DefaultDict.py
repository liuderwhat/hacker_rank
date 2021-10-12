'''
5 2
a
a
b
a
b
a
b

1 2 4
3 5
'''

from collections import defaultdict

ga, gb = list(map(int, input().split()))

a = defaultdict(list)

for i in range(1, ga+1):
    a[input()].append(i)

res = []
for _ in range(gb):
    b = input()
    if b not in a.keys():
        res.append([-1])
    else:
        res.append(a[b])


[print(*i) for i in res]

# for _ in range(gb):
#     word = input()
#     a['b'].append(word)
#     # if word == 'a':
#     #     a['a'].append(word)
#     # else :
#     #     a['b'].append(word)

# for i in a.items():
#     print(i)
