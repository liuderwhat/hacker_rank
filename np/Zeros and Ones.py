import numpy

'''
3 3 3
'''

shape = list(map(int, input().split()))

print(numpy.zeros(shape, dtype = numpy.int)) 
print(numpy.ones(shape, dtype = numpy.int)) 
