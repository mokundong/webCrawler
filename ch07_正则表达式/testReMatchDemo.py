import re
match = re.search(r'[1-9]\d{5}','BIT100081')
if match:
    print(match.group(0))
print(type(match))
print(match.string)
print(match.pos)
print(match.endpos)
print(match.start())
print(match.end())
print(match.span())