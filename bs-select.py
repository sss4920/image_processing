# css선택자 사용하기

from bs4 import BeautifulSoup

html="""
<html><body>
<div id="meigen">
    <h1>위키북스 도서</h1>
    <ul class="items">
        <li>유니티 게임 이펙트 입문</li>
        <li>스위프트</li>
        <li>모던</li>
    </ul>
</div>
</body></html> 
"""
soup = BeautifulSoup(html, 'html.parser')
h1 = soup.select_one("div#meigen > h1").string
print(h1)
li_list = soup.select("div#meigen > ul.items > li")
print(li_list)
for x in li_list:
    print("li: ", x.string)