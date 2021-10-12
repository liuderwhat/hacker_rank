

size = list(int(num) for num in input().strip().split())

b = '.|.'
middle = size[0] // 2
for i in range(size[0]//2 +1) : 
    
    if i == middle:
        print('WELCOME'.center(size[1],'-'))
    else:
        print((b * (2*i+1)).center(size[1],'-'))

for i in range(middle-1, -1, -1) : 
    print((b * (2*i+1)).center(size[1],'-'))