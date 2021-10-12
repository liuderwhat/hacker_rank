


def poisson_dis(num_list):
    
    cost_machineA = 160 + 40 * (num_list[0] + pow(num_list[0], 2))
    cost_machineB = 128 + 40 * (num_list[1] + pow(num_list[1], 2))
    
    print('{:.3f}'.format(cost_machineA))
    print('{:.3f}'.format(cost_machineB))

num_list = list(float(num) for num in input().strip().split())


'''
num_list[0] : machine A
num_list[1] : machine B
'''
poisson_dis(num_list)