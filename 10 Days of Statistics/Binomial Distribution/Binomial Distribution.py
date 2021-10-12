# Enter your code here. Read input from STDIN. Print output to STDOUT

# with exactly 6 children will have at least  3 boys?

def combination(n, r):
    # n!/r!(n-r)!
    t1, t2, t3 = 1, 1, 1
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

def binomial_function(n, r, p, q):

    binomial_p = 0

    for i in range(r, 7):

        combination_value = combination(n, i)
        boy_p = p / (p + q)
        
        binomial_p = binomial_p + combination_value * pow(boy_p, i) * pow(1 - boy_p, n-i)
    return binomial_p
    
burn_ratio = list(float(num) for num in input().strip().split())
print('{:.3f}'.format(binomial_function(6, 3, burn_ratio[0], burn_ratio[1])))