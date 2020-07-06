import requests
from bs4 import BeautifulSoup
from mkdir import mkDir
import os
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    'connection':'close'
}
#获取图片链接和标题
def getInfo(url,headers):
    srcs = []
    titles = []
    soup =  BeautifulSoup(requests.get(url,headers = headers).text,'html.parser')
    #获取图片链接
    for img in soup.find_all('img',class_='card-img-top'):
        srcs.append(img['src'])
    #获取标题
    for title in soup.find_all('h5',class_='card-title'):
        titles.append(title.text)
    return srcs,titles

url = 'http://www.testclass.net/all'
srcs,titles = getInfo(url,headers)

dir = mkDir('f:\\pyfiles\\web\\')

def downLoad(src,name,dir):
    print('downding %s'%name)
    local_filename = dir + "\\" + name + src.split('/')[-1]
    r = requests.get(src,stream = True,headers = headers)
    with open (local_filename,'wb') as f:
        #f.write(r.content)
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                # chunk = os.path.join(dir,local_filename)
                f.write(chunk)
                f.flush()
for src,title in zip(srcs,titles):
    dir1 = mkDir('f:\\pyfiles\\web\\'+title)
    downLoad(src,title,dir1)



