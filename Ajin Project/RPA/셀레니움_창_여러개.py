from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options=Options()
chrome_options.add_experimental_option("detach",True)

#불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])

Service=Service(executable_path=ChromeDriverManager().install())
driver= webdriver.Chrome(service=Service,options=chrome_options)

# 웹페이지 해당 주소 이동
driver.get("https://google.com/")
time.sleep(2)

driver.execute_script('window.open("https://naver.com")')
time.sleep(2)

driver.switch_to.window(driver.window_handles[0]) #처음넣은거
time.sleep(2)

driver.close() #창 닫기

print(driver.window_handles)

