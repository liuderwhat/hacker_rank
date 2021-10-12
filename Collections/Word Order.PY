'''
4
bcdef
abcdefg
bcde
bcdef

3
2 1 1
'''
from collections import OrderedDict

n = int(input())
word_dic = OrderedDict()

for _ in range(n):
    word = input()
    word_dic.setdefault(word, 0)
    word_dic[word] += 1

print(len(word_dic))
print(*word_dic.values())