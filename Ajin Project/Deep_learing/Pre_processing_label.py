# Example 폴더 안의 이미지 -> Example.1.jpg , Example.2.jpg , ....

import os

# data 폴더 경로
data_folder_dir = '../data/train/'  # train 폴더 경로
dir_list = (os.listdir(data_folder_dir))  # train 하위 경로 list (짧)

print(dir_list)
for dataName in dir_list:  # train 하위 경로
    data_dir = f'../data/train/{dataName}'  # train 하위 경로 (김)

    # data 폴더 안에 있는 모든 파일에 대해서 반복문 실행
    for i, filename in enumerate(os.listdir(data_dir)):  # 이미지들로 반복
        # 파일 이름이 .jpg or .png 로 끝나는 경우에만 이름 변경
        if filename.endswith(('.jpg', '.png')):
            src = os.path.join(data_dir, filename)
            dst = os.path.join(data_dir, f'{dataName}.{i}.jpg')
            os.rename(src, dst)
