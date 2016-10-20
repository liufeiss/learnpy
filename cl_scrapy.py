import re
import requests
from bs4 import BeautifulSoup

url = 'http://cl.aueyq.com/htm_data/16/1610/2101445.html'
header = {'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

r = requests.get(url, headers=header)
print(r.encoding)
print(r.text)





