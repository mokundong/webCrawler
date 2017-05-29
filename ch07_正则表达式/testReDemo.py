import re
#searchDemo
print("======searchDemo======")
match = re.search(r'[1-9]\d{5}','BIT 100081')
if match:
    print(match.group(0))

#matchDemo
print("======matchDemo======")
match = re.match(r'[1-9]\d{5}','100081 BIT fa')
if match:
    print(match.group(0))

#findallDemo
print("======findallDemo======")
ls = re.findall(r'[1-9]\d{5}','BIT100081 YSU100084')
print(ls)

#splitDemo
print("======splitDemo======")
ls = re.split(r'[1-9]\d{5}','BIT100081 YSU100084')
rs = re.split(r'[1-9]\d{5}','BIT100081 YSU100084',maxsplit=1)
print(ls)
print(rs)

#finditer
print("======finditer======")
for m in re.finditer(r'[1-9]\d{5}','BIT100081 YSU100084'):
    if m:
        print(m.group(0))

#subDemo
print("======subDemo======")
ss =  re.sub(r'[1-9]\d{5}',':zipcode','BIT100081 YSU100084')
print(ss)