if __name__ == '__main__':
    s = input()
    '''
    print True if  has any alphanumeric characters. Otherwise, print False.
    print True if  has any alphabetical characters. Otherwise, print False.
    print True if  has any digits. Otherwise, print False.
    print True if  has any lowercase characters. Otherwise, print False.
    print True if  has any uppercase characters. Otherwise, print False.
    '''
    
    print (any(c.isalnum() for c in s))
    print (any(c.isalpha() for c in s))
    print (any(c.isdigit() for c in s))
    print (any(c.islower() for c in s))
    print (any(c.isupper() for c in s))
