from bs4 import BeautifulSoup
import requests
r = requests.get("http://python123.io/ws/demo.html")
# print(r.text)
demo = r.text
soup = BeautifulSoup(demo,"html.parser")
print(soup.a.prettify())
# print(soup.title)
# print(soup.a)