'''
2
.*\+
.*+

True
False
'''

import re 

def isvalidregex(regex):
    try: re.compile(regex)
    except re.error: return False
    return True

ans = []
for _ in range(int(input())):
    ans.append(isvalidregex(input()))

[print(i) for i in ans]


