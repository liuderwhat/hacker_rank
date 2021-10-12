'''
Decimal
Octal
Hexadecimal (capitalized)
Binary
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
'''
import string

alphabet_list = list(string.ascii_uppercase)
def Octal(i):
    o_list = []
    tmp1 = 0
    tmp2 = 0
    if i >= 8:

        while(i >= 8):
            tmp1 = i // 8
            tmp2 = i % 8

            o_list.insert(0, tmp2 % 8)
            if tmp1 < 8:
                o_list.insert(0, tmp1 % 8)

            i = tmp1
    else : 
        return str(i % 8)
    o_str = ''

    for i in o_list:
        o_str = o_str + str(i)
    return o_str

def Hex(i):
    h_list = []
    
    if i >= 16:
        while(i >= 16):
            tmp1 = i // 16
            tmp2 = i % 16

            if tmp2 < 16 :

                if tmp2 >= 10:
                    h_list.insert(0, alphabet_list[tmp2%10])
                else : 
                    h_list.insert(0, tmp2 % 16)

            if tmp1 < 16 :
                if tmp1 >= 10:
                    h_list.insert(0, alphabet_list[tmp1%10])
                else : 
                    h_list.insert(0, tmp1 % 16)

            i = tmp1
    else : 
        if i >= 10:
            return alphabet_list[i%10]
        else : 
            return str(i % 16)

    h_str = ''
    for i in h_list:
        h_str = h_str + str(i)
    return h_str

def Binary(i):
    b_list = []
    
    if i >= 2:
        while(i >= 2):
            tmp1 = i // 2
            tmp2 = i % 2

            if tmp2 < 2 :
                if tmp2 == 0:
                    b_list.insert(0, tmp2)
                else : 
                    b_list.insert(0, tmp2)

            if tmp1 < 2 :
                if tmp1 == 1:
                    b_list.insert(0, tmp1)
            i = tmp1
    else : 
        return str(i % 2)

    b_str = ''
    for i in b_list:
        b_str = b_str + str(i)
    return b_str

def print_formatted(number):



    width = len(bin(number)[2:])
    for i in range(1, number+1):
        # print(str(i).rjust(width), Octal(i).rjust(width), Hex(i).rjust(width), Binary(i).rjust(width))
        print(str(i).rjust(width), oct(i)[2:].rjust(width), hex(i)[2:].upper().rjust(width), bin(i)[2:].rjust(width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)