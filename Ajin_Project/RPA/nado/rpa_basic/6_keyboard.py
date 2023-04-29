import pyperclip
import pyautogui
w = pyautogui.getWindowsWithTitle("메모장")[0]
w.activate()

# pyautogui.write("12345")
# pyautogui.write("NadoCoding", interval=0.25)
# pyautogui.write("나도코딩")

# pyautogui.write(['t', 'e', 's', 't', 'left',
#                 'left', 'right', 'l', 'a', 'enter'], interval=0.25)


# pyautogui.write("$")
# 특수문자
# shift 4-> $
# pyautogui.keyDown("shift")  # shift 키를 누른 상태에서
# pyautogui.press("4")  # 숫자 4를 입력하고
# pyautogui.keyUp("shift")  # shift 키를 뗀다

# pyautogui.hotkey("ctrl", "alt", "shift", "a") # 앞에 있는거 부터 누르고 뒤에 있는거부터뗌


# pyperclip.copy("나도코딩")  # 문자열 클립보드에 저장
# pyautogui.hotkey("ctrl", "v")

# 함수화
def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")


my_write("나도코딩")

# 자동화 프로그램 종료
# win: ctrl + alt + del
