s = input()
def getKey(x):
    if x.islower():
        return(2,x)
    elif x.isupper():
        return(1,x)
    elif x.isdigit() :
        if int(x)%2==1:
            return(3,x)
        else :
            return(4,x)

print(sorted(s,key=getKey))
# upper = []
# lower = []
# odd = []
# even = []

# for i in s:

#     if i.isalpha() and i.islower():

#         lower.append(i)
#     elif i.isalpha() and i.isupper():
#         upper.append(i)

#     elif i.isdigit() :

#         if int(i)%2:
#             odd.append(i)
#         else:
#              even.append(i)
       

# lower.sort()
# upper.sort()
# odd.sort()
# even.sort()

# lower.extend(upper)
# lower.extend(odd)
# lower.extend(even)

# print(''.join(lower))
