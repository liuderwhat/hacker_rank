'''
4 3 2 
1 2
1 2 
1 2
1 2
3 4
3 4
3 4 

n*p m*p

[[1 2]
 [1 2]
 [1 2]
 [1 2]
 [3 4]
 [3 4]
 [3 4]] 
'''

import numpy as np

n, m, p = list(map(int, input().split()))

a_matrix = []
b_matrix = []

for _ in range(n):
    a_matrix.append(list(map(int, input().split()[:p])))

for _ in range(m):
    b_matrix.append(list(map(int, input().split()[:p])))

a_matrix = np.array(a_matrix)
b_matrix = np.array(b_matrix)

print(np.concatenate((a_matrix, b_matrix)))

