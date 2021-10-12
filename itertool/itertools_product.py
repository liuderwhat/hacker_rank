from itertools import product

# (x,y) for x in A for y in B)
# print(list(product([1, 2, 3], repeat = 2)))
'''
[(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)]
'''
# A = [[1, 2, 3], [4, 5, 6]]

# print(list(product(*A)))

'''
 1 2
 3 4

 1, 3) (1, 4) (2, 3) (2, 4)
'''

a = list(int(num) for num in input().strip().split())
b = list(int(num) for num in input().strip().split())

print(*list(product(a, b)))