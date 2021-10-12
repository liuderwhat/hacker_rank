'''
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6   

78.00
'''
from collections import namedtuple
num_stu = int(input())
avg_list = []
stus = namedtuple('stus', input())

for _ in range(num_stu):
    col_val = input().split()
    stu = stus(col_val[0], col_val[1], col_val[2], col_val[3])
    avg_list.append(int(stu.MARKS))
print(round(sum(avg_list) / len(avg_list),2))
