import pyautogui
# pyautogui.FAILSAFE=False #모퉁이에 마우스를 위치하면 프로그램 동작이 멈추는데 그걸 무효화시킴
# pyautogui.mouseInfo()
pyautogui.PAUSE = 1  # 모든 동작에 1초씩 sleep 적용

for i in range(5):
    pyautogui.move(100, 100)
