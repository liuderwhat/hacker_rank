
'''
CDXXI
True
'''


import re
regex_pattern = r"[IVXLCDM]"   # Do not delete 'r'.
print(str(bool(re.match(regex_pattern, input()))))