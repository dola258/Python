from bs4 import BeautifulSoup
                #파스칼 표기법은 무조건 클래스

html_doc = """
<html>
<body>

<h1>H1태그</h1>
<div class='a'>클래스 찾기 - a</div>
<div class='b'>클래스 찾기 - b</div>
<div class='b'>클래스 찾기 - b2</div>
<div id='hello'>아이디 찾기</div>

<div id='focusPanelCenter'>
    <div class='panel_inner'>
        <img alt='국민일보'>a입니다</img>
    </div>
</div>


</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

#print(soup.prettify())

#img 태그 안에 alt찾기: id->class->img
target = soup.select_one("#focusPanelCenter .panel_inner img")
print(target)
title = target["alt"]
print(title)

# 태그안에 내용만 
target2 =soup.select_one(".b")
print(target2.text)

# HTML 엘레멘트 = DOM
#바디 전체 찾기
m_body = soup.body
#print(m_body)

#h1 태그 찾기
m_h1 = soup.h1
#print(m_h1)

#class='a' 찾기
m_a = soup.find(class_='a')
#print(m_a)

#class='b' 찾기
m_b = soup.find(class_='b')
#print(m_b)

#같은 클래스이름 찾기(리스트 타입)
m_b_all = soup.find_all(class_='b')
#print(m_b_all)
#print(m_b_all[-1])

#id로 찾기
m_hello = soup.find(id='hello')
#print(m_hello)








