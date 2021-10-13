'''
4 3
1 7 2 4

3
'''
from collections import Counter

def nonDivisibleSubset(k, s):
    # Write your code here
    c = Counter((i%k for i in s))

    count = 0
    blacklist = set()

    for x, y in c.most_common():

        if x == k / 2 or x == 0:
            count += 1

        elif k - x not in blacklist:

            count += y

            blacklist.add(x)

    return count
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)