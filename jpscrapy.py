import re
import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timedelta
import matplotlib.pylab as pl

url = 'http://flights.ctrip.com/domesticsearch/search/SearchFirstRouteFlights?DCity1=NKG&ACity1=HAK&SearchType=S&DDate1=2017-01-14&IsNearAirportRecommond=0&rk=2.1584177185657594220045&CK=086439AFD44F56D3D35BA7B105A0380F&r=0.0596633525027611486411'
header = {'User-Agent':r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}
r = requests.get(url, headers=header)
js = r.text

dic = json.loads(js)
price_dic = dic['lps']
print(price_dic)


now = datetime.now()
print(now)

min = 900
minday = ''
pr = []
for i in range(90):
    day = now+timedelta(days=i)
    day1 = day.strftime('%Y-%m-%d')
    price = price_dic[day1]
    pr.append(price)
    if price > 0 and price < min:
        min = price
        minday = day1

pl.plot(range(90), pr)

print(minday+"'s price will be most cheap it is only "+str(min))

with open('js.txt', 'w+') as f:
    f.write(str(price_dic))

pl.show()




