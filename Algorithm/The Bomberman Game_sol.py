r,c,n = [int(i) for i in input().split()]
s= set([])
for i in range(r):
    t = list(input())
    for j in range(c): 
        if t[j] == 'O': s.add((i,j))


if n==1:
    final = [['.' for i in range(c)] for j in range(r) ]
    for x in s: final[x[0]][x[1]] = 'O'
    for x in final:
        print(*x, sep ='')
elif n%2 == 0:
    for i in range(r):
        print(*['O' for i in range(c)], sep ='')
else:
    for _ in range((5-n%4)//2):
        final = [['O' for i in range(c)] for j in range(r) ]
        for x in s:
            
            final[x[0]][x[1]] = '.'
            if x[0] >=1: final[x[0]-1][x[1]] = '.'
            if x[0] <=r-2:final[x[0]+1][x[1]] = '.'
            if x[1]>=1:final[x[0]][x[1]-1] = '.'
            if x[1]<= c-2:final[x[0]][x[1]+1] = '.'
        
        s=set([])
        for i in range(r):
            for j in range(c):
                if final[i][j] == 'O':s.add((i,j))
    for x in final:
        print(*x, sep ='')