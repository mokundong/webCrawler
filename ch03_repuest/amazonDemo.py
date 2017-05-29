import requests
url = "https://www.amazon.cn/dp/B06XW5PPLN/ref=sr_1_9?s=wireless&ie=UTF8&qid=1496034930&sr=1-9"
try:
    # kv = {'user-agent':'Mozilla/5.0'}
    # r = requests.get(url,headers=kv)
    r = requests.get(url)
    
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("ERROR")

