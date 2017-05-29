import requests

url = "http://www.baidu.com"
r = requests.get(url)
# print(r.status_code)
# print(type(r))
# print(r.headers)
r.encoding = "utf-8"
print(r.text)

