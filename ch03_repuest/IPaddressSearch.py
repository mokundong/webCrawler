import requests
url = "http://ip.chinaz.com/"
ip = '210.41.99.46'

try:
    r = requests.get(url+ip)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:2000])
except:
    print("爬取失败")