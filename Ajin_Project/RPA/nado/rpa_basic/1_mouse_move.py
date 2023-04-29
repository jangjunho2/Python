import pyautogui

size = pyautogui.size()  # 화면 사이즈 가져옴
print(size)  # [0]=width [1]=height

# 마우스 이동
pyautogui.moveTo(100, 100, 1)  # 지정한 위치로 이동 #절대좌표
pyautogui.move(100, 100, 1)  # 상대좌표 이동

# 마우스좌표
p = pyautogui.position()
print(type(p), p)
print(p[0], p[1])
print(p.x, p.y)
