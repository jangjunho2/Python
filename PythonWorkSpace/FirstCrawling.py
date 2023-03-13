import requests
from bs4 import BeautifulSoup

#네이버와 대화시도
response =requests.get("https://www.naver.com")

#네이버에서 html줌
html =response.text

#html 번역선생님으로 수프 만듬
soup = BeautifulSoup(html,'html.parser')

# id 가 #NM_set_home_btn 인 놈 한개를 찾아냄
word= soup.select_one('#NM_set_home_btn')
print(word)
print(word.text)
