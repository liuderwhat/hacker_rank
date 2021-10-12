import numpy

n, m = list(int(num) for num in input().split())
matrix = []
for _ in range(n):
    matrix.append(list(int(num) for num in input().split()[:m]))
    
matrix = numpy.array(matrix)

print(numpy.transpose(matrix))
print(matrix.flatten())
