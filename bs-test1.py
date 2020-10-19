from bs4 import BeautifulSoup

html = """
<html><body>
    <h1>스크레이핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

soup = BeautifulSoup(html, 'html.parser')

h1 = soup.html.body.h1
p1 = soup.html.body.p
p2 = p1.find_next_sibling("p") #교재에 있는대로하면 none 객체를 반환해 next_sibling을 사용할 수 없어서 이처럼 사용하자

print(h1)
print(p1)
print(p2)