# web2.py
#웹서버와 통신
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#웹봇(웹로봇)
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
soup = BeautifulSoup(data, "html.parser")

# <td class="title">
# 	<a href="/webtoon/detail?">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
cartoons = soup.find_all("td", class_="title")
print("갯수:", len(cartoons) )
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#기존 파일에 첨부(a+)
f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
for item in cartoons:
    title = item.text.strip()
    print(title)
    f.write(title + "\n")

f.close()




                        