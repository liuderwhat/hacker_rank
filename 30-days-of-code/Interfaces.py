'''
6

I implemented: AdvancedArithmetic
12
'''
class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        d_list = [i fot i in range(1, n+1) if not n % i]
        return sum(d_list)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)