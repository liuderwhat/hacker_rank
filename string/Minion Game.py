'''
Stuart has to make words starting with consonants.(子因)
Kevin has to make words starting with vowels(母音)
'''

def minion_game(string):

    s_score = 0
    k_score = 0
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    


    ####### so1 1 ##########
    # wordc_list = []
    # words_list = []
    # for i in range(len(string)): :
    #     tmp = i
    #     for i1 in range(i+1, len(string)+1):
    #         word = string[i:i1]
    #         if word[0] in vowels:
    #             if word not in wordc_list:
    #                 wordc_list.append(word)
    #                 k_score = k_score + 1
    #             else :
    #                 k_score = k_score + 1
    #         else :
    #             if word not in words_list:
    #                 words_list.append(word)
    #                 s_score = s_score + 1
    #             else :
    #                 s_score = s_score + 1

    ##########sol 2 ###############
    for i in range(len(string)):
        
        if string[i] in vowels:
            k_score = k_score + len(string)-i
        else :
            s_score = s_score + len(string)-i

    if s_score > k_score:
        print('Stuart', s_score, sep=' ')
    elif(k_score > s_score):
        print('Kevin', k_score, sep=' ')
    else:
        print('Draw')
# all(x in 'potato' for x in ['t','o','m','a'])
if __name__ == '__main__':
    s = input()
    minion_game(s)