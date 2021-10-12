'''
group() 
A group() expression returns one or more subgroups of the match.

groups()
A groups() expression returns a tuple containing all the subgroups of the match

groupdict()
A groupdict() expression returns a dictionary containing all the named subgroups of the match,
keyed by the subgroup name.

match() -------- >>> Determine if the RE matches at the beginning of the string.

search() --------->>> Scan through a string, looking for any location where this RE matches.

findall() --------->>> Find all substrings where the RE matches, and returns them as a list.

finditer()----->>> Find all substrings where the RE matches, and returns them as an iterator.


..12345678910111213141516171820212223

1
'''
import re

pattern = r'([a-zA-Z0-9])\1+'
m = re.search(pattern, input())

if m:
    print(m.group(1))
else:
    print(-1)


# http://120.105.184.250/cswang/thit/Linux/RegularExpression.htm