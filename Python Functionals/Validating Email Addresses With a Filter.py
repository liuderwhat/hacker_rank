'''
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
'''
#  username@websitename.extension
# maximum length of the extension is .３

'''
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.

'''

import re

def fun(s):
    # return True if s is a valid email, else return False
    mail_list = []
    mail_split = s.split('@')
    
    if len(mail_split) == 2:
        username = mail_split[0]
        
        if len(mail_split[1].split('.')) >= 2:

            websitename = mail_split[1].split('.')[0]

            extension = mail_split[1].split('.')[1:]

            if not(username and websitename and extension):
                return False

            for c in username:
                if not(c.isalpha() or c.isdigit() or c == '_' or c == '-'):
                    return False

            for c in websitename:
                if not(c.isalpha() or c.isdigit()):
                    return False

            for c in extension:
                if not(c.isalpha() and len(c)<=3):
                    return False
            
            return True

        else : 
            False
    else :
        return False

def fun2(s):
    a = re.match(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$',s)
    return(a)

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)