import requests
from bs4 import BeautifulSoup
import re
import urllib
from pathlib import Path

#初始化模块，发送requests请求，beautifulsoup解析html模块
url = 'http://daily.zhihu.com/'
head = {'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
'''
r = requests.get(url, headers=head)
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
#print(soup.prettify())
print(soup.find_all('img'))
'''

#发送请求拿到经美丽的汤整理后的汤（html）
def gethttp(url, head):
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup




#打印分割线模块
def fengexian():
    fgx = '='
    for i in range(100):
        fgx = fgx + '='
        print(fgx)

#匹配一个正确的http://xxxx.jpg的正则表达式模块
re_http = re.compile(r'^http\:\/\/[0-9a-zA-Z\.\/]*\.jpg$')

#筛选正确连接模块
def useablejpg(soup):
    jpg = []
    for s in soup.find_all('img'):
        src = s['src']
        if re_http.match(src):
            jpg.append(src)
    return jpg

#下载图片模块
def download(x, dir):
    for i in range(len(x)):
        y = 'text'+str(i)+'.jpg'
        path = dir/y
        with path.open('wb') as img:
            ri = requests.get(x[i], headers=head)
            img.write(ri.content)
    print('all downloads %s ' % len(x))

def setup_download_dir(dir_name):
    dir = Path(dir_name)
    if not dir.exists():
        dir.mkdir()
    return dir


soup = gethttp(url, head)
x = useablejpg(soup)
dir = setup_download_dir('img')
download(x, dir)









'''
h = 'http://hwafgjhywe.jpg'
h1 = '/img/afgeg.png'
h2 = 'http://pic2.zhimg.com/7bf3f3b878b0c8d6d98db74e491356b9.jpg'
re_http = re.compile(r'^http\:\/\/[0-9a-zA-Z\.\/]*\.jpg$')
print(re_http.match(h1))
'''

