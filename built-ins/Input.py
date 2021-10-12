'''
1 4
x**3 + x**2 + x + 1

True
'''

x, ans = list(int(num) for num in input().split())
poly = input()
# eval可以直接算公式的字串
print(eval(poly) == ans)