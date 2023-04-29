import pyautogui
pyautogui.sleep(3)  # 초대기
print(pyautogui.position())


# pyautogui.click(64, 16, 1)  # 좌표이동후 클릭

# # pyautogui.click()#위치 정보없으면 현재 위치클릭
# pyautogui.mouseDown()  # 마우스 누르기
# pyautogui.mouseUp()  # 마우스 떼기


# # pyautogui.doubleClick() #더블클릭
# pyautogui.click(clicks=2)  # clicks값만큼 클릭


# # 2번 #드래그 구현?
# pyautogui.moveTo(200, 200)
# pyautogui.mouseDown()  # 마우스 누르기
# pyautogui.moveTo(300, 300)
# pyautogui.mouseUp()  # 마우스 떼기


# pyautogui.rightClick()  # 우 클릭
# pyautogui.middleClick()  # 휠 클릭

# pyautogui.moveTo(1125, 21)
# pyautogui.drag(100, 0, 0.25)  # 너무 빠른동작으로 drag 수행이 안될때는 duration 값 설정

pyautogui.scroll(300)  # 양수이면 위 방향, 음수이면 아래방향으로 300만큼 스크롤
