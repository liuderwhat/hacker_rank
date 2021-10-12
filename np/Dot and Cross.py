'''
Print the matrix multiplication of A and B. (n*n)

2
1 2
3 4
1 2
3 4

[[ 7 10]
 [15 22]]

'''
import numpy as np

n = int(input())

a = []
b = []

for _ in range(n):
    a.append(list(map(int, input().split()[:n])))

for _ in range(n):
    b.append(list(map(int, input().split()[:n])))

a = np.array(a)
b = np.array(b)

print(np.dot(a, b))