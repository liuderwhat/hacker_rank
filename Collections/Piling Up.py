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
    
    # 先找出左邊與右邊的值
    # 並取最大值代表目前比較對象
    head, last = 0, len(c) - 1
    current = max([c[0], c[-1]])

    # 當比較對象找出來時，最大者會加一個索引值
    if current == c[0]:
        head += 1
    else:
        last -= 1

    # 只會比n-1次
    for _ in range(len(c)-1):
        
        # 判斷有無違反規則 : 不能比目前的值大
        if c[head] > current or c[last] > current:
            return 'No'
        # 若無違反則比較
        # 與一開始一樣，大者前進並指派給current
        else : 
            if c[head] >= c[last]:
                current = c[head]
                head += 1
            else:
                current = c[last]
                last -= 1
    # 若迴圈跑完代表都無違反規則
    else:
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
