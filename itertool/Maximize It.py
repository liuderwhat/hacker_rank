'''
3 1000 (K, M)
2 5 4 N integer #element in the list
3 7 8 9 
5 5 7 8 9 10

206
'''

from itertools import product

def pow2(i):
    return pow(i, 2)

def max_calcu(n_list, m):
    # 每個數字都取二次方
    pow2_num = [list(map(pow2, i)) for i in n_list]
    # 數組做排列組合
    res_num = list(product(*pow2_num))
    # 每個組合比較取最大的
    res_num_max = max([sum(i) % m for i in res_num])
    
    print(res_num_max)

k, m = list(int(num) for num in input().split())

calcu_list = []

for _ in range(k):
    # 取元素就好，大小不需要
    a = [int(num) for num in input().split()[1:]]
    calcu_list.append(a)

#(num of ele, list)
max_calcu(calcu_list, m)



