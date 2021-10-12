'''
Errors detected during execution are called exceptions.

Handling Exceptions
The statements try and except can be used to handle selected exceptions. 
A try statement may have more than one except clause to specify handlers for different exceptions.
'''

'''
3
1 0
2 $
3 1
'''

res = []
for test in range(int(input())):
    try:
        a,b = map(int,input().split()) 
        division_result = a // b
    except ZeroDivisionError as e:
        res.append('Error Code: '+e.args[0])
    except ValueError as e:
        res.append('Error Code: '+e.args[0])
    else:
        res.append(division_result)

[print(i) for i in res]