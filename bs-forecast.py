# urlopen()과 Beautifulsoup 조합하기
from bs4 import BeautifulSoup
import urllib.request as req

url ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser") # url 오픈하면 html파일등으로 인식되는듯

title = soup.find("title").string
wf = soup.find("wf").string
print(title)
print(wf)
