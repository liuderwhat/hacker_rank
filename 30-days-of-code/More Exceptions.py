'''
4
3 5
2 4
-1 -2
-1 3

243
16
n and p should be non-negative
n and p should be non-negative
'''

class Calculator():
        
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        return n**p
myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e) 