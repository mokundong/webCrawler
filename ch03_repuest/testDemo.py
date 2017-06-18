import requests

#url = "http://www.baidu.com"
url = "http://hps.mep.gov.cn/jsxm/npzxmgs/201704/t20170405_409325.shtml"
r = requests.get(url)
# print(r.status_code)
# print(type(r))
# print(r.headers)
r.encoding = "utf-8"
print(r.text)

