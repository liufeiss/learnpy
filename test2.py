import requests
from bs4 import BeautifulSoup
import re
import time
import random


'''
r = requests.get('http://www.baidu.com')
r.encoding = 'utf-8'
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
print('================================================================')
x = []
for a in soup.find_all('a'):
    print(a['href'])
    x.append(a['href'])
url = x[random.randint(0, len(x))]
r1 = requests.get(url)
#print(random.randint(0, len(x)))
print(r1)
'''
url = 'http://www.baidu.com'
for i in range(50):
    r = requests.get(url)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'html.parser')
    x = []
    for a in soup.find_all('a'):
        print(a['href'])
        print('=================================================================')
        x.append(a['href'])
    url = x[random.randint(0, len(x))]
    file = open('test2.txt', 'w')
    file.write(url+'\n')
file.close()


