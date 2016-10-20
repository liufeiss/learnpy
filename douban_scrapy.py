import re
import requests
from bs4 import BeautifulSoup

url = 'https://www.douban.com/location/nanjing/'
header = {'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

req = requests.get(url, headers=header)
soup = BeautifulSoup(req.text, 'html.parser')
print(soup.find_all('a'))



#print(req.encoding)


#print(req.text)







