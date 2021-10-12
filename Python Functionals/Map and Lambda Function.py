'''
map(function, iterables)
applies a function to every member of an iterable
'''

# print(list(map(len, ['abc', 'de','f'])))

'''
Lambda
a single expression anonymous function often used as an inline function.
'''
# length = lambda a : len(a)

# print(length('abc'))

'''
5

[0, 1, 1, 8, 27]
the cubes(^3) of the first n fibonacci numbers.
'''
def fibonacci(num):
    f_List = [0, 1]
    for i in range(2, num):
        f_List.append(f_List[i-2]+(f_List[i-1]))

    return f_List

fibonacci_rec = lambda y : y if y < 2 else fibonacci_rec(y-1) + fibonacci_rec(y-2)
# def cube(n):
#     return n ** 3
cube = lambda a : a ** 3

num = int(input())

print(list(map(cube, fibonacci(num))))