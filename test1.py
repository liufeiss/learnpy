import requests
import random
from time import sleep
import urllib
import re

def main():
    url = 'https://www.zhihu.com/question/22591304/followers'
    heards = {}
    i=1
    for x in range(20, 360, 20):
        data = {'start': '0', 'offset': str(x), '_xsrf': 'a128464ef225a69348cef94c38f4e428'}
        content = requests.post(url, data=data, timeout=10).text
        imges = re.findall('<img src=\\\\\\"(.*?)_m.jpg', content)
        for img in imges:
            try:
                img = img.replace('\\',)
                pic = img + ".jpg"
                path = r'C:\Users\aaa'
                urllib.urlretrieve(pic, path)
                print('yes')
                i+=1
                sleep(random.unifrom(0.5,1))
            except:
                print('out')
            sleep(random.uniform(0.5,1))

if __name__=='__main__':
    main()




