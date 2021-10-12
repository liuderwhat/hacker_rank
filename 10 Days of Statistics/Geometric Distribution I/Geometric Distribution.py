'''
The probability that a machine produces a defective product is 1/3. 
What is the probability that the 1st defect occurs the 5th item produced?
'''

def geometric_dis(ratio, n):
    defective_p = ratio[0] / ratio[1]

    geometric_p = pow(1-defective_p, n-1) * (defective_p)
    
    return geometric_p

ratio = list(int(num) for num in input().strip().split())

n = int(input().strip())
'''
numerator and denominato
ratio[0]:分子
ratio[1]:分母

n : inspection we want the probability of being the first defect for:
'''
print('{:.3f}'.format(geometric_dis(ratio, n)))
