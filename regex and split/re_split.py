'''
re.split()
The re.split() expression splits the string by occurrence of a pattern.
>>> import re
>>> re.split(r"-","+91-011-2711-1111")
['+91', '011', '2711', '1111']
'''

'''
100,000,000.000

all of the , and .

100
000
000
000
'''

import re
pattern = r'[,.]'
split_res = re.split(pattern, input())
[print(i) for i in split_res]