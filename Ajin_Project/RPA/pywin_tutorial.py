# pip install pywin32
# https://codetorial.net/pywin32/mouse_control.html

from win32api import GetLocalTime
from win32api import GetSystemMetrics
import win32api
import win32con
import win32gui
# 간단한 소리
# win32api.Beep(500, 1000)

# 마우스 커서 위치 얻기
pos = win32api.GetCursorPos()
print(pos)

# 마우스 커서 이동 시키기
# pos = (200, 200)
# win32api.SetCursorPos(pos)


# 마우스 클릭하기
def mouse_click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


# mouse_click(300, 300)

# 마우스 커서 영역 제한하기?

# (left, top, right, bottom) 영역으로 마우스 커서 제한하기
# win32api.ClipCursor((200, 200, 700, 700)) 탈출 ctrl alt del

# 마우스 커서 제한 해제하기
# win32api.ClipCursor((0, 0, 0, 0))
# win32api.ClipCursor()

# 스크린 해상도 얻기

print('Width:', GetSystemMetrics(0))
print('Height:', GetSystemMetrics(1))

# 화면 필셀 색상 얻기
color = win32gui.GetPixel(win32gui.GetDC(win32gui.GetActiveWindow()), 500, 500)
print(hex(color))

# 로컬 시간

print(GetLocalTime())
