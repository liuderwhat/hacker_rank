def stones(n, a, b):
    min_n = min(a, b)
    max_n = max(a, b)
    cur = min_n * (n-1) 
    max_score = (n-1) * max_n
    s = []
    while(cur <= max_score):
        s.append(cur)
        cur += (max_n-min_n)
    
    return s

if __name__ == '__main__':


    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)
        print(result)