from selenium import webdriver

browser=webdriver.Chrome("C:\chromedriver.exe")
browser.get("https://www.naver.com")

browser.get("https://www.google.com")

#크롬창이 네이버로 이동한 후 종료가 정상