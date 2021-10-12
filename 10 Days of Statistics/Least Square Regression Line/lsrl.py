'''
95 85
85 95
80 70
70 65
60 70
'''
# from sklearn import linear_model
# import numpy as np

# def lr(math, stat):
#     mathl = np.asarray(math).reshape(-1, 1)
#     statl = np.asarray(stat).reshape(-1, 1)
#     lm = linear_model.LinearRegression()
#     lm.fit(mathl, statl)
#     print(round(lm.predict(np.array([80]).reshape(-1, 1))[0][0], 3))
def lr(n, math, stat, math_test):
    xy = [math[i]*stat[i] for i in range(n)]
    x_squ = [pow(math[i], 2) for i in range(n)]
    x_mean = sum(math) / n
    y_mean = sum(stat) / n

    b = (n * sum(xy) - sum(math)*sum(stat)) / ((n * sum(x_squ)) - pow(sum(math), 2))
    a = y_mean - b * x_mean
    
    stat_pred = a + b * math_test
    print(round(stat_pred, 3))

n = 0
math_test = 80
contents = []
while n <= 4:
    try:
        stu_score = list(int(num) for num in input().strip().split())
    except EOFError:
        break
    contents.append(stu_score)
    n = n + 1

math_score = [i[0] for i in contents]
stat_score = [i[1] for i in contents]

lr(5, math_score, stat_score, math_test)