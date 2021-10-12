'''
5
12 9 61 5 14

True 

Condition 1: All the integers in the list are positive.
Condition 2: 5 is a palindromic integer

You are given a space separated list of integers. If all the integers are positive, then you need to check if any integer is a palindromic integer.
'''
# def ispalindromic(n):
    
#     length = len(str(n))
#     i = 0
#     flag = True
#     if n < 10:
#         return True
#     else:
#         while(flag):
#             if i <= length:
#                 r = (n / pow(10, i)) % 10
#                 l = n // pow(10, length-1)
#                 if r == l:
#                     return True
#             else :
#                 flag = False
#             i = i +1
#     return False

# num = int(input())

# num_list = list(int(num) for num in input().split())

# print(all([i>0 for i in num_list]) and  any([ispalindromic(i) for i in (num_list)]))

#Three line
num = int(input())
num_list = list(num for num in input().split())
print(all([int(i)>0 for i in num_list]) and any([i == i[::-1] for i in num_list]))

a = '12321'
# start at string length, end at position 0, move with the step -1 (or one step backward).
# print(a == a[len(a):0:-1])
print(a[len(a)::-1])