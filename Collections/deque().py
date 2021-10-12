'''
6
append 1
append 2
append 3
appendleft 4
pop
popleft

1 2
'''

from collections import deque

d = deque()
n = int(input())

for _ in range(n):

    method, *args = list(i for i in input().split())
    getattr(d, method)(*args)

print(*list(d), sep =' ')