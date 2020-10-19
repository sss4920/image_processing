from bs4 import BeautifulSoup
import urllib.request as req
import datetime

url = "http://finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res,'html.parser')

price = soup.select_one("div.market1 > div.data > ul.data_lst > li.on > a > div > span.value").string
print("usd/krw", price)

t = datetime.date.today()
fname = t.strftime("%Y-%m-%d") +".txt"
with open(fname, "w", encoding="utf-8") as f:
    f.write(price) 