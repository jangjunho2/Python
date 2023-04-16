import os

name = input()
# data 폴더 경로
data_dir = f'../data/train/{name}'

# data 폴더 안에 있는 모든 파일에 대해서 반복문 실행
for i, filename in enumerate(os.listdir(data_dir)):
    if filename.endswith(('.jpg', '.png')):  # 파일 이름이 .jpg or .png 로 끝나는 경우에만 이름 변경
        src = os.path.join(data_dir, filename)
        dst = os.path.join(data_dir, f'{name}.{i}.jpg')
        os.rename(src, dst)
