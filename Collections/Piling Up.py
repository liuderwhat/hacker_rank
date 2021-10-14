'''
2
6
4 3 2 1 3 4
3
1 3 2

Yes
No
'''

from collections import deque


# method 1
for _ in range(int(input())):

    _, queue = input(), deque(map(int, input().split()))

    for cube in reversed(sorted(queue)):
        if queue[-1] == cube:
            queue.pop()
        elif queue[0] == cube:
            queue.popleft()
        else:
            print('No')
            break
    # for/else : check loop's completion
    else:
        print('Yes')

# method 3
def is_cude(c):

    head, last = 0, len(c) - 1
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

# method 4
def is_cude(c):

    head, last = 0, len(c) - 1
    
    while (head < last and c[head] >= c[head+1]):
        head += 1
    while (head < last and c[head] <= c[head+1]):
        head += 1

    if head == last: 
        print('Yes')
    else :
        print('No')

# method 2
def check_stack(cube_length):
    
    stack = []
    l = 0
    r = len(cube_length)-1
    flag = True
    for x in range(len(cube_length)):
        if flag:
            if cube_length[l] < cube_length[r]:

                if not(stack):
          
                    stack.append(cube_length[r])
                    r -= 1
                else:
          
                    if cube_length[r] <= stack[x-1]:
                        stack.append(cube_length[r])
                        r -= 1
                    else:
                        flag = False

            elif cube_length[l] >= cube_length[r]:
        
                if  not(stack):
                    stack.append(cube_length[l])
                    l += 1
                else:
        
                    if cube_length[l] <= stack[x-1]:
                        stack.append(cube_length[l])
                        l += 1
                    else:
                        flag = False
        else:
            break
    return flag

t = int(input())
ans = []
for _ in range(t):
    cube = int(input())
    cube_length = list(int(num) for num in input().split()[:cube])
    ans.append(check_stack(cube_length))

for i in ans:
    if i:
        print('Yes')
    else:
        print('No')
