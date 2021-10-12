def solve(s):
    s_spilt = s.split()
    
    space_list = [i for i, v in enumerate(s) if not v.isalnum() ]
    dis = 1
    tmp = 0
    dis_list = []
    # print(space_list)

    for i, v in enumerate(space_list) :
        if not tmp:
            tmp = v
        else : 
            if v - tmp == 1:
                dis = dis + 1
                tmp = v
            else:
                dis_list.append(dis)
                dis = 1
                tmp = v
        if space_list[-1] == v:
            dis_list.append(dis)
    dis_list.append(0)
    new_list = []
    ans = ''
    # print(dis_list)
    for i, v in enumerate(s_spilt):
        v = list(v)
        if v[0].isalpha():
            v[0] = v[0].upper()
        v = ''.join(v)

        new_list.append(v+' '*dis_list[i])
    ans = ans.join(new_list)

    return ans

def solve2(s):

    for x in s.split():
        if len(x) > 1:
            new_x = x[0].capitalize() + x[1:]
            s = s.replace(x, new_x)

def solve3(s):

    ans = []
    pre_space = False
    
    for i, v in enumerate(s):
        
        if i == 0:
            ans.append(v.upper())

        elif v == ' ':
            pre_space = True
            ans.append(' ')

        elif v and pre_space:
            ans.append(v.upper())
            pre_space = False

        elif v and (not pre_space):
            ans.append(v)

    return ''.join(ans)

def solve4(s):

    pre_space = True
    string = list(s)
    for i, c in enumerate(string) :

        if  c.isalpha() or c.isdigit():
            string[i] = c.upper()
            pre_space = False
        else:
            pre_space = True

    return ''.join(string)
    
if __name__ == '__main__':

    s = input()

    result = solve(s)
    result2 = solve4(s)
    print(result2)
