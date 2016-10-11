import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.taobao.com')
print(r.encoding)
soup = BeautifulSoup(r.text, 'html.parser')
with open('text1_2.txt', 'w') as f1:
    f1.write(r.text)
#print(soup.prettify())

print(soup.title)
#print(soup.head)
print(soup.a)
print(soup.a.string)


