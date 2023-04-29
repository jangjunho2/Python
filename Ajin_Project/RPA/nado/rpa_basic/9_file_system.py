# 파일 기본
import os
# print(os.getcwd())  # current working directory 현재 작업공간
# os.chdir("School")
# print(os.getcwd())
# os.chdir("..")
# print(os.getcwd())
# os.chdir("../..")
# print(os.getcwd())
# os.chdir("C:/")
# print(os.getcwd())


# 파일 경로
file_path = os.path.join(os.getcwd(), "my_file.txt")  # 절대 경로 생성
print(file_path)
