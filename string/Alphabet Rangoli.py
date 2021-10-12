import string
alphabet_list = list(string.ascii_lowercase)

def goli_top(alpha_list, alpha, n):
    max_alpha = alpha % n
    for i in range(n-1, max_alpha, -1):
        alpha_list = alpha_list+alphabet_list[i]
    for i in range(max_alpha, n):
        alpha_list = alpha_list+alphabet_list[i]
    return alpha_list

def goli_bottom(alpha_list, alpha, n):
    max_alpha = alpha % n
    for i in range(n-1, max_alpha, -1):
        alpha_list = alpha_list+alphabet_list[i]
    for i in range(max_alpha, n):
        alpha_list = alpha_list+alphabet_list[i]
    return alpha_list

def print_rangoli(n):
    alphabet_list = list(string.ascii_lowercase)
    ran_list = ''
    for i in range(n, 0, -1):
        ran_list = ran_list + alphabet_list[i-1]
    for i in range(1, n):
        ran_list = ran_list + alphabet_list[i]
    tmp = '-'.join(ran_list)
    size = len(tmp)
    
    for i in range(n-1, -1, -1):
        alpha_list = ''
        tmp = goli_top(alpha_list, i, n)
        tmp = '-'.join(tmp)
        print(tmp.center(size, '-'))

    for i in range(1, n):
        alpha_list = ''
        tmp = goli_top(alpha_list, i, n)
        tmp = '-'.join(tmp)
        print(tmp.center(size, '-'))

    # for i in range(n, 0, -1):
    #     print('-'*(i-1)*2 + alphabet_list[i-1] + '-'*(i-1)*2)

num = int(input())
alrangoli(num)
