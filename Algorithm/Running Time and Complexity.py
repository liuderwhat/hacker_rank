import math
import timeit

def isPrime(n):

    for i in range(2, n//2+1):

        if not n % i:

            return False
    if n == 1:
        return False
    return True

def isPrime2(n):

    for i in range(2, n):

        if not n % i:

            return False
        i = i**2

    if n == 1:
        return False
        
    return True

def isPrime3(n):
    if n == 1:
        return False
    elif n == 2:
        return True

    for i in range(2, math.ceil(math.sqrt(n))+1):

        if not n % i:
            return False

    return True

start = timeit.default_timer()
for _ in range(int(input())):

    num = int(input())

    if isPrime2(num):

        print('Prime')

    else:

        print('Not prime')
stop = timeit.default_timer()

print('Time: ', stop - start)  
