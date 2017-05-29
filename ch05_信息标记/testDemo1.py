from bs4 import BeautifulSoup
import requests
import re
url = "http://python123.io/ws/demo.html"
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")

#需找标签
# print(soup.find_all(['a','b']))
#打印所有标签名字
# for tag in soup.find_all(True):
#     print(tag.name)
#打印以b开头的标签
# for tag in soup.find_all(re.compile('b')):
#     print(tag.name)

#查找包含link属性信息
# attrs = soup.find_all(id=re.compile("link"))
# print(attrs)

#是否对子孙全部检索
