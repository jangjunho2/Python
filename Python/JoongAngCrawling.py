import requests
from bs4 import BeautifulSoup 
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def printOnWeb():
    return render_template('index.html',testDataHtml=result,link=link)




header = {'User-agent': 'Mozila/2.0'}
response = requests.get("https://www.joongang.co.kr/politics",headers=header)
html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
titles = soup.select_one('#story_list>li>div>h2')
result=titles.text.strip()
link=titles.select_one('a')['href']


if __name__ =="__main__":
    app.run()


