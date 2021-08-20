# web1.py 
#웹 문서를 검색하는 라이브러리
from bs4 import BeautifulSoup

#파일을 로딩(연속으로 함수나 메서드를 호출: 메서드 체인)
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성(html, xml)
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )
#<p>를 전부 검색 ==> List객체로 리턴 
#print( soup.find_all("p") )

#<p class="outer-text">컨텐츠</p>: 필터링
print( soup.find_all("p", class_="outer-text") )







