# myset = {1, 2}

# myset = set()

# myset = set(['m', 'a', 'b'])
# myset2 = set(['a', 'b'])

# print('issubset : ', myset2.issubset(myset))
# print('isdisjoint : ', myset2.isdisjoint(myset))
# print('union : ', myset2.union(myset))
# print('intersection : ', myset2.intersection(myset))
# print('difference : ', myset2.difference(myset))
# print('symmetric_difference : ', myset2.symmetric_difference(myset))

n, m = input().split()

sc_ar = input().split()

A = set(input().split())
B = set(input().split())


print([(i in A) - (i in B) for i in sc_ar])