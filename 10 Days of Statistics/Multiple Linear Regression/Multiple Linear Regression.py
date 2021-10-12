'''
2 7
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
4
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18
'''

import numpy as np

def mutiple_lr(b, y, q):
    
    b_np = np.array(b)
    y_np = np.array(y)
    q_np = np.array(q)
    # x transpose
    x_dash  = b_np.T
    # product of x_dash and x
    X = np.dot(x_dash, b_np)
    # inverse of X
    X_inv = np.linalg.inv(X)
    # producet of X_inv and x_dash
    X_final = np.dot(X_inv, x_dash)
    # product of X_final and y i.e B
    B = np.dot(X_final, y)
    # calculate the y_pred
    # y_pred = np.matmul(q, B)
    # b_val = np.matmul(np.matmul(np.linalg.inv(np.matmul(b_np.T, b_np)), b_np.T), y_np)
    
    # calculate the y_pred
    for i in q:
        print(round(np.matmul(B, i), 2))

num_list = list(int(num) for num in input().strip().split())

b_matrix = [list(float(num) for num in input().strip().split())[:num_list[0]+1] for i in range(num_list[1])]

b = [[1]+i[:len(i)-1] for i in b_matrix]

y = [i[-1] for i in b_matrix]
# print(b_matrix)
q_number = int(input())

q_matrix = [list(float(num) for num in input().strip().split())[:num_list[0]] for i in range(q_number)]
q = [[1]+i[:len(i)] for i in q_matrix]

mutiple_lr(b, y, q)


