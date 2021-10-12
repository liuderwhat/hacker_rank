import numpy as np

'''
1.1 2 3
0

3.0
'''


a = list(map(float, input().split()))

print(np.polyval(a, float(input())))