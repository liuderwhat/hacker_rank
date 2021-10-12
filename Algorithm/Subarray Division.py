def birthday(s, d, m):
    # Write your code here
    res = []
    m_count = 0
    
    if len(s) == 1:
        if s[0] == d:
            return 1
        else:
            return 0
        
    for i in range(len(s)):
        if i+m <= len(s):
            if sum(s[i:i+m]) == d:
                m_count+=1
        else:
            break

    return m_count

def  birthday2(s, d, m):
    m_count = 0

    l = len(s)
    if l >= m:

        res = sum(s[:m])

        if res == d:

            m_count += 1

        for x in range(m, l):

            res += s[x] - s[x-m]

            if res == d:

                m_count += 1
    return m_count


n = int(input().strip())

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])

result = birthday2(s, d, m)

print(result)