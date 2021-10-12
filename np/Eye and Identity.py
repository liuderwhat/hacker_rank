'''
3 3

[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]

'''
import numpy
# get alignment correct
numpy.set_printoptions(legacy='1.13')

n, m = list(map(int, input().split()))
print(numpy.eye(n, m))