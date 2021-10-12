
def permutation(x, y, z, n):

    permu_list = [[num1, num2, num3] for num1 in range(x+1) for num2 in range(y+1) for num3 in range(z+1) if sum([num1, num2, num3]) is not n]
    print(permu_list)

x = int(input()) 
y = int(input())
z = int(input())
n = int(input()) # remove the sum that is equal to n

permutation(x, y, z, n)
