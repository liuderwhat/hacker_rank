'''
STDIN   Function
-----   --------
3       __elements[] size N = 3
1 2 5   __elements = [1, 2, 5]

4

3
1 2 5
'''
from itertools import combinations

class Difference:
    def __init__(self, a):
        self.__elements = a

    # Add your code here
    def computeDifference(self):
        self.res = [list(i) for i in combinations(self.__elements, 2)]
        self.diff_res = [abs(i[1] - i[0]) for i in self.res]
        self.maximumDifference = max(self.diff_res)

# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)