'''
10
10 9.8 8 7.8 7.7 7 6 5 4 2
200 44 32 24 22 17 15 12 8 4
'''
import math 

def pearson(n, x, y):
    
    mu_x = sum(x) / n
    mu_y = sum(y) / n

    squr_dis_x = [pow((i - mu_x), 2) for i in x]
    squr_dis_y = [pow((i - mu_y), 2) for i in y]
    std_x = math.sqrt((sum(squr_dis_x) / len(x)))
    std_y = math.sqrt((sum(squr_dis_y) / len(y)))

    p_sum = 0
    for i in range(n):
        p_sum = p_sum + (x[i] - mu_x) * (y[i] - mu_y)

    print(round(p_sum / (n * std_x * std_y), 3) )
   
input_num = int(input())
x_list = list(float(num) for num in input().strip().split())[:input_num]
y_list = list(float(num) for num in input().strip().split())[:input_num]
pearson(input_num, x_list, y_list)