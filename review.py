'''
2            
6            
4 3 2 1 3 4  
3            
1 3 2 

'''
num_all = []

def is_cude(c):

    last, head = 0, len(c) - 1
    current = max([c[0], c[-1]])

    if current == c[0]:
        head += 1
    else:
        last -= 1

    for _ in range(len(c)-1):
        
        if c[head] > current or c[last] > current:
            return 'No'
        else : 
            if c[head] >= c[last]:
                current = c[head]
                head += 1
            else:
                current = c[last]
                last -= 1

    return 'Yes'

for _ in range(int(input())):
    num = int(input())
    num_list = list(map(int, input().split()[:num]))
    num_all.append(num_list)


[print(is_cude(i)) for i in num_all]

