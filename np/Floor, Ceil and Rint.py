'''
1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]
'''
import numpy as np
np.set_printoptions(legacy='1.13')

num_list = list(map(float, input().split()))
num_list = np.array(num_list)
print(np.floor(num_list), np.ceil(num_list), np.rint(num_list), sep='\n')