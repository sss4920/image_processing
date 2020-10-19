# 네이버 금융에서 환율정보 추출하기
from bs4 import BeautifulSoup
import urllib.request as req

url = "http: //finance.naver.com/marketindex/"
res = req.urlopen(url)

soup = BeautifulSoup(res,"html.parser")
price = soup.select_one("div.head_info > span.value").string
print("usd/krw =", price)