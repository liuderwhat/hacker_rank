'''
5

1
121
12321
1234321
123454321
'''
# def print_tri(i):
#     tri_list = [x for x in range(1, i+1)]
#     ans_list = []
#     ans_list.extend(tri_list)
#     for x in range(len(tri_list)-1,0,-1):
#         ans_list.append(x)
#     ans = ''
#     for i in ans_list:
#         ans += str(i)
#     return ans

# num = int(input())

# for i in range(1, num+1):
#     print(print_tri(i))

for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print((pow(10, i) // 9) ** 2)