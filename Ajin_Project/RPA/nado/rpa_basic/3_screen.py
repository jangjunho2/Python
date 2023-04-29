import pyautogui
# 스크린 샷 찍기
# img = pyautogui.screenshot()
# img.save("screenshot.png")  # 파일로 저장


# pyautogui.mouseInfo()
# 29,16 65,171,242 #41ABF2

pixel = pyautogui.pixel(29, 16)  # 픽셀 색 저장
print(pixel)  # 색 출력

print(pyautogui.pixelMatchesColor(29, 16, pixel))  # 픽셀값이 일치하면 True
