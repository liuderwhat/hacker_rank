

def chocolateFeast(n, c, m):

    ch = n // c
    count = 0
    s = 0
    while(ch >= m):

        
        w = ch // m
        count += m*w
        s = ch - m*w
        ch = w + s

    if not count:
        return ch
    else : 
        return count+ch
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        print(result)

'''
3
10 2 5
12 4 4
6 2 2 
'''