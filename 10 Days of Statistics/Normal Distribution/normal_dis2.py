'''
Normal Distribution II

mean = 70 
sigma = 10

g > 80
g >= 60
g < 60

70 10
80
60
'''


import math

def cdf(stat, ran_val):
    
    return 0.5 * (1 + math.erf( (ran_val - stat[0]) / (stat[1] * pow(2, 0.5)) ) )

def normal_dist(stat, num1, num2):

    normal_q1 = (1 - cdf(stat, num1) )* 100
    normal_q2 = (1 - cdf(stat, num2) )* 100
    normal_q3 = cdf(stat, num2) * 100

    print('{:.2f}'.format(normal_q1))
    print('{:.2f}'.format(normal_q2))
    print('{:.2f}'.format(normal_q3))

stat = list(float(num) for num in input().strip().split())
num1 = float(input())
num2 = float(input())



'''
stat[0] : mean
stat[1] : std
'''

normal_dist(stat, num1, num2)


