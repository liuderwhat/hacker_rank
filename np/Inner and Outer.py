'''
you are given two array, a,b 
compute their inner and outer product

0 1
2 3

3
[[0 0]
 [2 3]]
'''
import numpy as np
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = np.array(a)
b = np.array(b)

print(np.inner(a, b), np.outer(a, b), sep='\n')