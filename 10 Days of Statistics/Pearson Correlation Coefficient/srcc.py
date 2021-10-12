'''
10
10 9.8 8 7.8 7.7 1.7 6 5 1.4 2 
200 44 32 24 22 17 15 12 8 4
'''
import math 
import copy

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

    return round(p_sum / (n * std_x * std_y), 3)

# Spearman's rank correlation coefficien
def spearman(n, x, y):
    # x_tmp = copy.deepcopy(x)
    # y_tmp = copy.deepcopy(y)
    x_tmp = list(set(x))
    y_tmp = list(set(y))
    
    x_tmp.sort()
    y_tmp.sort()

    r_x = [index+1 for i in x for index, v in enumerate(x_tmp) if i == v]
    r_y = [index+1 for i in y for index, v in enumerate(y_tmp) if i == v]
    
    if len(x_tmp) == n and len(y_tmp) == n:
        sp_sum = 0
        for i in range(n):
            sp_sum = sp_sum + pow(r_x[i] - r_y[i], 2)
        print(round(1 - ((6 * sp_sum) / (n * (pow(n, 2) - 1))),3))

    else : 
        
        print(pearson(n, r_x, r_y))

input_num = int(input())
x_list = list(float(num) for num in input().strip().split())[:input_num]
y_list = list(float(num) for num in input().strip().split())[:input_num]
spearman(input_num, x_list, y_list)