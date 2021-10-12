
from collections import Counter

'''
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

200
'''
num_shoe_size  = int(input())
shoe_size = list(map(int, input().split()))
size_counter = Counter(shoe_size)

total_earn = 0
for _ in range(int(input())):
    size, price = list(map(int, input().split()))
    if size_counter[size] > 0:
        total_earn += price
        size_counter[size] = size_counter.get(size, 0) - 1
    
print(total_earn)