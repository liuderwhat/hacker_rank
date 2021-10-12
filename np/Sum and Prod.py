'''
2 2
1 2
3 4

24
'''
import numpy as np

n, m = list(map(int, input().split()))

matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split()[:m])))

print(np.prod(np.sum(matrix, axis = 0)))