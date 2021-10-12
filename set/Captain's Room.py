'''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
'''

g_num = int(input())
room_num = list(int(num) for num in input().strip().split())
s1 = set() # unique room number
s2 = set() # room number occurs more in once

for i in room_num:
    if i not in s1:
        s1.add(i)
    else : 
        s2.add(i)

print(s1.difference(s2).pop())
