import textwrap
'''
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ
'''
def wrap(string, max_width):
    return  "\n".join(textwrap.wrap(string, max_width))
        
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)