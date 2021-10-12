'''
aabbbccde

b 3
a 2
c 2
'''
from collections import OrderedDict

def com_logo():
    word_dic = OrderedDict()
    for c in string:

        word_dic.setdefault(c, 0)
        word_dic[c] += 1

    ans = [[key, value] for key,value in word_dic.items()]
    ans.sort()
    sorted_list = sorted(ans, key=lambda x: x[1], reverse = True)
    [print(i[0], i[1], sep=' ') for i in sorted_list[:3]]

def com_logo2(string):
    word_dic = OrderedDict()
    for c in string:

        word_dic[c] = word_dic.get(c, 0)+1  

    #Sorting Dict by value & storing sorted keys in Dict_keys.
    sorted_list = sorted(word_dic, key=word_dic.get, reverse=True)
    [print(i, word_dic[i], sep=' ') for i in sorted_list[:3]]

string = input()
com_logo2(string)