n, m = list(int(num) for num in input().split())

stu_score = []

for _ in range(m):
    stu_score.append(list(float(num) for num in input().split()))

# one_stu_score = list(zip(*stu_score))
[print(sum(i)/m) for i in list(zip(*stu_score))]