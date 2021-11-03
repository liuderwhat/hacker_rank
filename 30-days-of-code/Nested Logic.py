'''
9 6 2015 
6 6 2015

45
'''
def cal_fee(r, d):

    fee = 0

    # year
    if d[2] - r[2] < 0:

        fee = 10000

    elif d[2] - r[2] == 0:

        # month
        if d[1] - r[1] < 0:

            fee = abs(d[1] - r[1]) * 500

        elif d[1] - r[1] == 0:
            
            # day
            if d[0] - r[0] < 0:

                fee = abs(d[0] - r[0]) * 15
            # ontime
            else:
                return 0
        # ontime
        else:
            return 0
    # ontime
    else:
        return 0

    return fee

r = list(map(int, input().split()))
d = list(map(int, input().split()))

print(cal_fee(r, d))