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
# from konlpy.tag import Hannanum

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
    stop_words.append('would')  # 직접추가

    # hannanum = Hannanum()

    # In[2]:

    # pdf 갯수 입력
    nums_pdf = int(input("pdf 갯수 입력 : "))

    lines = ""

    path = input("경로(폴더명)를 입력하세요 (pdf,font 들어있는 폴더명..) : ")
    for i in range(nums_pdf):
        try:
            pdf_file = open(f'{path}/enJam{i}.pdf', 'rb')
            print(f"{path}/enJam{i}.pdf 읽는중 ...")
        except:
            print("파일을 찾을 수 없습니다 다시 시작 해주세요.")
            exit()
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            lines += page.extract_text()
        pdf_file.close()
    words = lines.lower()  # 소문자로

    lines_list = lines.splitlines()
    words_list = [lines.split() for line in lines_list]

    # In[4]:

    double_list = words_list
    single_list = [item for sublist in double_list for item in sublist]
    lines = single_list
    print("단어 갯수: {:,}".format(len(lines)))

    tokens = tokenizer.tokenize(words)
    stopped_tokens = [i for i in list((tokens)) if not i in stop_words]
    stopped_tokens2 = [i for i in stopped_tokens if len(i) > 1]

    # In[7]:

    nums_cloudword = int(input("wordcloud에 넣을 빈도 높은 단어 갯수 입력 : "))

    counter = Counter(stopped_tokens2)
    top_words = counter.most_common()[:nums_cloudword]
    dictionary = {}

    for tup in top_words:
        key = tup[0]
        value = tup[1]
        dictionary[key] = value

    font_path = f'{path}/Roboto-Light.ttf'

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
        print("\n구름에 들어갈 단어들: \n")  # 클라우드에 들어갈 것들 이상한거 보고 제거하기 (출력 윗 줄)
        print(dictionary)
        del_items = input("불필요 한거 입력(띄어쓰기로 구분)('종료' 입력시 종료): ").split()
        if del_items[0] == '종료':
            print("단어제거 종료")
            break
        for del_item in del_items:
            try:
                del dictionary[del_item]
            except:
                print("잘못 입력하셧습니다.")

    ###############################
    print(dictionary)  # 제거된 이후 결과 실행하면 나오는 줄중에 (밑에 줄)

    wordcloud = wordcloud.generate_from_frequencies(dictionary)
    array = wordcloud.to_array()

    # In[13]:

    if __name__ == '__main__':  # 대체 코드
        plt.show()
        fig = plt.figure(figsize=(10, 10))
        plt.axis("off")  # x,y축 없애기
        plt.imshow(array, interpolation="bilinear")
        plt.show()  # 보여주기
        fig.savefig(f'{path}/enJamsCloud.png')  # 파일이 저장되는 이름 ㅇㅇ
        print(f"사진위치: {path}/enJamsCloud.png")
