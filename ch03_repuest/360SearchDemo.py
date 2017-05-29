import requests
keyword = "Python"
url = "http://www.so.com/s"

try:
    kv = {'q':keyword}
    r = requests.get(url,params=kv)
    print(r.request.url)
    r.raise_for_status()
    print(len(r.text))
except:
    print("ERROR")
