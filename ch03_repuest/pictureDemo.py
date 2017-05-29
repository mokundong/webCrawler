import requests
import os
root = "D:\\work\\myWebCrawler\\pics\\"
url = "https://img14.360buyimg.com/n0/jfs/t4642/110/753072126/121222/5556881f/58d484a0N1d9d2ebf.jpg"
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else:
        print("文件已经存在")
except:
    print("爬取失败")