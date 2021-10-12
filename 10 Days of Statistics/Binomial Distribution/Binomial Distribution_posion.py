# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
A manufacturer of metal pistons finds that, on average,  of the pistons they manufacture are rejected
 because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

No more than 2 rejects?
At least 2 rejects?
'''

def combination(n, r):
    # n!/r!(n-r)!
    t1, t2, t3 = 1, 1, 1

    # fact
    for i in range(n, 0, -1):
        t1 = t1 * i
    for i in range(r, 0, -1):
        t2 = t2 * i
    for i in range(n-r, 0, -1):
        t3 = t3 * i

    return t1 / (t2 * t3)

# def fact(n):
#     return 1 if n == 0 else n*fact(n-1)

# def comb(n, x):
#     return fact(n) / (fact(x) * fact(n-x))

def binomial_function(n, r, p):

    binomial_p_almost = 0
    binomial_p_aleast = 0

    # almost
    for i in range(r+1):

        combination_value = combination(n, i)
        
        binomial_p_almost = binomial_p_almost + combination_value * pow(p, i) * pow(1 - p, n-i)
    
    # aleast
    for i in range(r, n+1):

        combination_value = combination(n, i)
        
        binomial_p_aleast = binomial_p_aleast + combination_value * pow(p, i) * pow(1 - p, n-i)
    

    print('{:.3f}'.format(binomial_p_almost))
    print('{:.3f}'.format(binomial_p_aleast))

pos_reject = list(int(num) for num in input().strip().split())
'''
pos_reject[0] : posion ratio
pos_reject[1] : batch of pistons 
'''
binomial_function(pos_reject[1], 2, pos_reject[0] / 100)