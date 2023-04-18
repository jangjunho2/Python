import requests
from bs4 import BeautifulSoup
import html

days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
url = "https://coop.gwnu.ac.kr/contents.asp?page=848"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

for i in range(1, 22):
    if i % 3 == 1:
        print('\n\t\t\t\t\t', days[i//3], '\n')
        continue

    if i % 3 == 2:
        print('\t중식\n')
    else:
        print('\t석식\n')

    menu_text = soup.select_one(
        f"#diet_1_1 > div.table-responsive > table > tbody > tr:nth-child({i}) > td.left").decode_contents()

    menu_items = menu_text.split("<br/>")
    menu_items[-1] = '\n\n'
    for menu_item in menu_items:
        decoded_output = html.unescape(menu_item)
        print(decoded_output)
