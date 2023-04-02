from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# 셀레니움 4 버전 작동

# 크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager


import time
import pyautogui
import pyperclip
######################################################################
######################################################################
######################################################################
######################################################################
######### 네이버 아이디, 비밀번호 입력 ##################################
naverId = "TESTID"
naverPw = "TESTPW"
email_ad = "test@exaple.com"
#####################################################################
######################################################################
######################################################################
######################################################################
######################################################################

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메세지 없애기
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

Service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=Service, options=chrome_options)

# 웹페이지 해당 주소 이동
driver.implicitly_wait(5)  # 웹페이지가 로딩 될때까지 5초는 기다림
driver.maximize_window()  # 화면 최대화
driver.get(
    "https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")


# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click()
# id.send_keys(naverId) # 봇인거 걸림
pyperclip.copy(naverId)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)


# 비밀번호 입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
# pw.send_keys(naverPw) #봇인거 걸림
pyperclip.copy(naverPw)
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login > span")
login_btn.click()
time.sleep(2)

# 매일함 이동
driver.get("https://mail.naver.com")
time.sleep(2)

# 메일 쓰기 버튼 클릭  98,258
# driver.find_element(By.CSS_SELECTOR,"#root > div > nav > div > div.lnb_header > div.lnb_task > a.item.button_write > span").click()
pyautogui.moveTo(98, 258)  # 윗 줄 코드 css선택자가 이상함 제대로 안따짐...
pyautogui.click()
time.sleep(2)

# 받는사람
pyautogui.write(email_ad, interval=0.15)
pyautogui.press("tab")
pyautogui.press("tab")
time.sleep(2)

# 제목
pyperclip.copy("이것이 진짜 제목이다.")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")
time.sleep(2)

# 본문
pyperclip.copy("이것이 진짜 내용이다.")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

# 보내기 버튼 클릭
send_btn = driver.find_element(
    By.CSS_SELECTOR, "#content > div.mail_toolbar.type_write > div:nth-child(1) > div > button.button_write_task")
send_btn.click()
time.sleep(2)
