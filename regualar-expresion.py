import re
pattern =re.compile('search')
string = 'search this inside of this text please!'

a = print(pattern.search(string))
b = print(pattern.findall(string))
c = print(pattern.fullmatch(string))
d = print(pattern.match(string))