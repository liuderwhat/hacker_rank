'''
9800
49
205
15
'''
import math

def cdf(x, mu, sigma):
    z_score = (x - mu) / sigma
    return 0.5 * (1 + math.erf(z_score/  pow(2,0.5)))

def clt(max_weight, box_num, mean_weight, sigma_wight):
    mu_sum = box_num * mean_weight
    sigma_sum = pow(box_num, 0.5) * sigma_wight
    print(round(cdf(max_weight, mu_sum, sigma_sum), 4))


max_weight = float(input())
box_num = float(input())
mean_weight = float(input())
sigma_wight = float(input())

clt(max_weight, box_num, mean_weight, sigma_wight)