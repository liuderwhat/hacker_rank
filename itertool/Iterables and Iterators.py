'''
4 
a a c d
2

0.8333
'''
from itertools import combinations

def prok(letter, num_k):
    get_indice = [str(i+1) for i, v in enumerate(letter) if v == 'a']
    string = [str(i) for i in range(1, len(letter)+1)]
    res = [i for i in combinations(string, num_k)]
    score = 0
    for i in res:
        for x in get_indice:
            if x in i:
                score  = score +1
                break
    print(score / len(res))

def prok2(letter, num_k):
    res = [i for i in combinations(letter, num_k)]
    score = 0
    for i in res:
        if 'a' in i:
            score += 1
    print(score / len(res))

def prok2(letter, num_k):
    # string = [str(i) for i in range(1, len(letter)+1)]
    res = [i for i in combinations(letter, num_k)]
    fil = filter(lambda c : 'a' in c , res)
    print(len(list(fil)) / len(res))

num = int(input())

letter = input().split()

num_k = int(input())

prok2(letter, num_k)