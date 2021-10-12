'''
10 lenght of AB
10 length og BC

45
'''
import math

len_ab = int(input())
len_bc = int(input())

len_ac = pow(pow(len_ab, 2) + pow(len_bc, 2), 0.5)

res = int(round(180 - 90 - math.degrees(math.acos(len_bc/len_ac))))

degree=chr(176)
degree_sign = u"\N{DEGREE SIGN}"
print(res,degree_sign, sep='')