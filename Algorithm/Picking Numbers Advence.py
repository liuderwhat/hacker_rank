'''
calculate and find the max consecutive value of a list

4 6 5 3 3 1

because of the max is 3 3 4 5 6 
the answer is the length of the maximan of list : 5

1 2 2 4 5 6 7 8 10 12 13 14 15 16 17 18
ans: 7
'''

# input_num = int(input())
num = list(map(int , input().split()))

l = sorted(list(set(num)))

c = 0
ans = []
for i in range(len(l)):
    c += num.count(l[i])

    if num.count(l[i]+1) == 0:

        ans.append(c)
        c = 0

print(max(ans))
'''
1234678
'''