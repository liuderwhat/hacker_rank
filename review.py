import math

def encryption(s):

    row, col = math.floor(math.sqrt(len(s))), math.ceil(math.sqrt(len(s)))

    return [s[i::col] for i in range(col)]

if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result)