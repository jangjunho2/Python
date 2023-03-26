#!/usr/bin/env python
# coding: utf-8

# 그냥 학교에서 교양으로 txt가져와서 단어구름 했던거 가지고 pdf 여러장으로도 만들어본거..
# 친구 단어구름 필요하다해서 해본거 최적화 X 돌아는감..
#
# wordcloud 설치 오류 날떄 참고:
# https://hcid-courses.github.io/TA/FAQ/python_wordcloud_troubleshoot.html

# In[1]:


# pip install Pillow numpy pandas PyPDF2 nltk wordcloud konlpy google-colab
# pip install wordcloud --use-pep517
from konlpy.tag import Hannanum


# input=sys.stdin.readline
# from google.colab import drive
# drive.mount('/content/drive')

hannanum = Hannanum()


def get_nouns(line):
    return hannanum.nouns(line)


if __name__ == '__main__':
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import numpy as np
    from PIL import Image
    import konlpy
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    from nltk.stem.porter import PorterStemmer
    from collections import Counter
    import nltk
    import PyPDF2
    import pandas as pd
    import sys
    from collections import Counter

    tokenizer = RegexpTokenizer('[\w]+')

    nltk.download('stopwords')
    stop_words = stopwords.words('english')

    # hannanum = Hannanum()

    # In[2]:

    # pdf 갯수 입력
    nums_pdf = int(input("pdf 갯수 입력 : "))

    lines = ""
    path = input("경로(폴더명)를 입력하세요 (pdf,font 들어있는 폴더명..) : ")

    for i in range(nums_pdf):

        try:
            pdf_file = open(f'{path}/krJam{i}.pdf', 'rb')
            print(f"{path}/krJam{i}.pdf 읽는중 ...")
        except:
            print("파일을 찾을 수 없습니다 다시 시작 해주세요.")
            exit()
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            lines += page.extract_text()

        pdf_file.close()

    lines_list = lines.splitlines()
    words_list = [lines.split() for line in lines_list]

    def flatten(l):
        flatList = []
        for elem in l:
            if type(elem) == list:
                for e in elem:
                    flatList.append(e)
            else:
                flatList.append(elem)
        return flatList

    # In[4]:

    double_list = words_list
    single_list = [item for sublist in double_list for item in sublist]
    lines = single_list
    print("단어 갯수: {:,}".format(len(lines)))  # lines로 적었지만 사실 단어갯수임ㅋㅋ

    # In[5]:

    import multiprocessing

    num_cores = multiprocessing.cpu_count()
    print(f"총 {num_cores}개의 코어가 감지되었습니다.")

    # In[8]:

    btn = input("코어 사용? y/n 으로 입력하세요 : ")

    if btn == 'y':
        using_process = int(input("사용할 코어 갯수 입력 : "))
        print("진행된 횟수 안뜸..")
        from multiprocessing import Pool

        if __name__ == '__main__':
            with Pool(processes=using_process) as p:
                # temp = p.map(get_nouns, lines[:100], chunksize=10)  # 이걸로 테스트
                temp = p.map(get_nouns, lines, chunksize=10)  # 실제 코드
    else:
        print("코어 사용 X")
        temp = []
        for i in range(100):
            if i % 10000 == 0:
                print(f"{i:,}")
            temp.append(hannanum.nouns(lines[i]))  # 명사만 저장
    print("명사 확인 종료")

    # In[7]:

    nums_cloudword = int(input("wordcloud에 넣을 빈도 높은 단어 갯수 입력 : "))

    word_list = flatten(temp)
    word_list = [x for x in word_list if len(x) > 1]
    counter = Counter(word_list)
    top_words = counter.most_common()[:nums_cloudword]
    dictionary = {}

    for tup in top_words:
        key = tup[0]
        value = tup[1]
        dictionary[key] = value
    # In[11]:

    font_path = f'{path}/NanumBarunGothic.ttf'

    wordcloud = WordCloud(
        font_path=font_path,
        width=800,
        height=800,
        background_color="white"
    )

    wordcloud = wordcloud.generate_from_frequencies(dictionary)

    def __array__(self):
        """Convert to numpy array.
        Returns
        -------
        image : nd-array size (width, height, 3)
            Word cloud image as numpy matrix.
        """
        return self.to_array()

    def to_array(self):
        """Convert to numpy array.
        Returns
        -------
        image : nd-array size (width, height, 3)
            Word cloud image as numpy matrix.
        """
        return np.array(self.to_image())

    array = wordcloud.to_array()
    # 밑에 불필요한거 입력
    while True:
        print("\n구름에 들어갈 단어들: \n")
        print(dictionary)
        del_items = input("불필요 한거 입력(띄어쓰기로 구분)('break' 입력시 종료): ").split()
        if del_items[0] == 'break':
            print("단어제거 종료")
            break
        for del_item in del_items:
            try:
                del dictionary[del_item]
            except:
                print("잘못 입력하셧습니다.")

    print(dictionary)

    wordcloud = wordcloud.generate_from_frequencies(dictionary)
    array = wordcloud.to_array()

    # In[13]:

    if __name__ == '__main__':
        plt.show()
        fig = plt.figure(figsize=(10, 10))
        plt.axis("off")  # x,y축 없애기
        plt.imshow(array, interpolation="bilinear")
        plt.show()
        fig.savefig(f'{path}/krJamsCloud.png')  # 파일이 저장되는 이름
        print(f"사진위치: {path}/krJamsCloud.png")
