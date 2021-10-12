'''
3
07895462130
919875641230
9195969878

may have +91, 0, 91 written before 10 actual numbers

+91 78954 62130
+91 91959 69878
+91 98756 41230
'''

def wrapper2(f):
    def fun(l):
        # complete the function
        a_number = []
        for i in l:
            if len(i) > 10:
                ac_num = i[len(i)-10: len(i) - 5] + ' ' +i[len(i)-5:]
                a_number.append("+91 "+ac_num)
            else:
                ac_num = i[:5] + ' ' + i[5:]
                a_number.append("+91 "+ac_num)

        return f(a_number)
    return fun

def wrapper(f):
    def fun(l):
        # complete the function
        return f(('+91 '+ c[-10:-5]+' '+c[-5:] for c in l))
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)