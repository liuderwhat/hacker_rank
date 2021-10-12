import re

'''
Print the tuple in this format: (start _index, end _index).
If no match is found, print (-1, -1).

aaadaa
aa

(0, 1)  
(1, 2)
(4, 5)
'''

text, pattern = input(), input()
m= list(re.finditer("(?=(%s))"%pattern, text))
if not m:
    print((-1,-1))
for i in m:
    
    print((i.start(1),i.end(1)-1))