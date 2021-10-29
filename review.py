n = int(input().strip())
p = list(map(int,input().strip().split(' ')))


res = [p.index(p.index(i+1)+1)+1 for i in range(n)]
print(res)