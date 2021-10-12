'''
1 4
1 2 3 4
5 6 7 8

[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]]
'''
import numpy

n, m = list(map(int, list(input().split())))

array_a = []
array_b = []

for _ in range(n):
    array_a.append(list(map(int, list(input().split()[:m]))))

for _ in range(n):
    array_b.append(list(map(int, list(input().split()[:m]))))
array_a = numpy.array(array_a)
array_b= numpy.array(array_b)


print(array_a+array_b, array_a-array_b, array_a*array_b, array_a//array_b, array_a%array_b, array_a**array_b, sep='\n')