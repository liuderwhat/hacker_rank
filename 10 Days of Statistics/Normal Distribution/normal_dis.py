
import math

def cdf(stat, ran_val):
    
    return 0.5 * (1 + math.erf( (ran_val - stat[0]) / (stat[1] * pow(2, 0.5)) ) )

def normal_dist(stat, q1, q2):

    normal_q1 = cdf(stat, q1)
    normal_q2 = cdf(stat, q2[1]) - cdf(stat, q2[0])

    print('{:.3f}'.format(normal_q1))
    print('{:.3f}'.format(normal_q2))

stat = list(float(num) for num in input().strip().split())
q1 = float(input())
q2 = list(float(num) for num in input().strip().split())

'''
stat[0] : mean
stat[1] : std
'''

normal_dist(stat, q1, q2)