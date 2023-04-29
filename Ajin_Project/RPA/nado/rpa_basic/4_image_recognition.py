import pyautogui
import time
import sys

# file_menu = pyautogui.locateOnScreen("file_menu.png")
# print(file_menu)
# pyautogui.click(file_menu)

# 이미지 찾을때 시간이 좀 걸릴수있음 #못찾으면 none반환
# output = pyautogui.locateOnScreen("output.png")
# print(output)
# pyautogui.moveTo(output)


# for i in pyautogui.locateAllOnScreen("checkbox.png"):  # 잘못찾을수도있음
#     print(i)
#     pyautogui.click(i)

# 속도 개선

# 1.GrayScale
# output = pyautogui.locateOnScreen("output.png", grayscale=True)
# print(output)
# pyautogui.moveTo(output)

# 2.범위 지정
# output = pyautogui.locateOnScreen(
#     "output.png", region=(125, 653, 592-125, 768-653))
# print(output)
# pyautogui.moveTo(output)

# 3.정확도 조정
# for i in pyautogui.locateAllOnScreen("checkbox.png", confidence=0.9): #정확도 0.9이상이면 실행 opencv 설치 필요
#     print(i)
#     pyautogui.click(i)

# 자동화 대상이 바로 보여지지 않는 경우


# notepad_file_btn = pyautogui.locateOnScreen("notepad_file_btn.png")
# if notepad_file_btn:
#     pyautogui.click(notepad_file_btn)
# else:
#     print("발견 실패")


# 계속 기다리기
# notepad_file_btn = None
# while notepad_file_btn is None:
#     notepad_file_btn = pyautogui.locateOnScreen("notepad_file_btn.png")
#     print("발견 실패")

# pyautogui.click(notepad_file_btn)
# print("\n발견 완료")


# 2. 일정 시간동안 기다리기 (TimeOut)


# timeout = 10  # 10초 대기
# start = time.time()  # 시작 시간 설정
# notepad_file_btn = None
# while notepad_file_btn is None:
#     notepad_file_btn = pyautogui.locateOnScreen("notepad_file_btn.png")
#     print("발견 실패")
#     end = time.time()

#     if end - start > timeout:
#         print("시간 종료")
#         sys.exit()


# 함수화
def find_target(img_file, timeout=30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end-start > timeout:
            break
    return target


def my_click(img_file, timeout=30):
    target = find_target(img_file, timeout)
    if target:
        pyautogui.click(target)
    else:
        print(
            f"[Timeout {timeout}s] Target not found ({img_file}). Terminate program")
        sys.exit()


my_click("notepad_file_btn.png")
