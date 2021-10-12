'''
STDIN       Function
-----       --------
4           set a size M = 4
2 4 5 9     a = {2, 4, 5, 9}
4           set b size N = 4
2 4 11 12   b = {2, 4, 11, 12}

print their symmetric difference in ascending order.

5
9
11
12
'''

def sym_diff(a_set, b_set):
    sym =  list(a_set.symmetric_difference(b_set))
    sym.sort()
    for i in sym: print(i)


a_size = int(input())
a_set = set(int(num) for num in input().strip().split())

b_size = int(input())
b_set = set(int(num) for num in input().strip().split())
sym_diff(a_set, b_set)