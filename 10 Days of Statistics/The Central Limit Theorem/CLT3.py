'''
100
500
80
.95
1.96
'''
import math

pop_num = float(input())
mean = float(input())
sigma = float(input())
interval = float(input())
z_score = float(input())

sd_sample = sigma / (pop_num**0.5)
print(round(mean - sd_sample*z_score,2))
print(round(mean + sd_sample*z_score,2))