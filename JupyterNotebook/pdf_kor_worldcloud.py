'''
그냥 학교에서 교양으로 txt가져와서 단어구름 했던거 가지고 pdf 여러장으로도 만들어본거..
친구 단어구름 필요하다해서 해본거 최적화 X 돌아는감..
'''


###########################################
from google.colab import drive
drive.mount('/content/drive')

!pip install konlpy 
!pip install PyPDF2 

import pandas as pd
import PyPDF2
import nltk
from wordcloud import WordCloud 
from collections import Counter

from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import konlpy
from konlpy.tag import Hannanum 

tokenizer = RegexpTokenizer('[\w]+')

nltk.download('stopwords')
stop_words = stopwords.words('english')


hannanum = Hannanum() 
#########################################################
#########################################################
#########################################################
# pdf 갯수 입력
nums_pdf=1 # @개
lines = ""

for i in range(nums_pdf): 
  #한국어 전용 파일이름 krJam0.pdf , krJam1.pdf 무조건 0부터 해야함 
  # pdf_file = open(f'/content/drive/My Drive/wordcloud/krJam{i}.pdf', 'rb') #경로 맞게 수정
  pdf_file = open(f'/content/drive/My Drive/krJam{i}.pdf', 'rb') #한국어 전용 파일이름 krjam0.pdf , kerJam1 
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
##################################################################################
##################################################################################
##################################################################################
double_list=words_list
single_list = [item for sublist in double_list for item in sublist]
lines=single_list
print(len(lines)) #저번에 한개 햇을떄 683만이었나 그거보다 크면 될듯?
##################################################################################
##################################################################################
##################################################################################

############################# 오래걸림##########주의########
temp = [] 
for i in range(len(lines)):
    print(lines[i]) #줠라김... #되는지 테스트 중단하고 ctrl+/ 하고 다시 실행 ㄱㄱ
    temp.append(hannanum.nouns(lines[i])) #명사만 저장

##################################################################################
##################################################################################
##################################################################################
from PIL import Image
import numpy as np

word_list=flatten(temp)
word_list=pd.Series([x for x in word_list if len(x)>1])
word_list.value_counts().head(30) #wordcloud에 넣을 빈도 높은 숫자 @개 추출


# font_path = '/content/drive/My Drive/wordcloud/NanumBarunGothic.ttf' #워드클라우드 이미지 생성 시 사용할 글꼴 파일 경로를 지정합니다.
font_path = '/content/drive/My Drive/NanumBarunGothic.ttf' #워드클라우드 이미지 생성 시 사용할 글꼴 파일 경로를 지정합니다.

wordcloud = WordCloud(
    font_path = font_path,
    width = 800, #가로크기 #저장하는거에 영향 미침ㅇㅇ
    height = 800, #세로크기
    background_color="white" #뒷 배경
)

count = Counter(word_list) 
wordcloud = wordcloud.generate_from_frequencies(count) 

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
print(count) # 클라우드에 들어갈 것들 이상한거 보고 제거하기 (출력 윗 줄)
#####밑에 불필요한거 입력
del_items=['제1','제2'] #불필요한거 입력 ㄱㄱ

for del_item in del_items:
  del count[del_item]
###############################
print(count) # 제거된 이후 결과 실행하면 나오는 줄중에 (밑에 줄)

wordcloud = wordcloud.generate_from_frequencies(count)
array = wordcloud.to_array()
##################################################################################
##################################################################################
##################################################################################
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


fig = plt.figure(figsize=(10, 10) )# 얼마나 크게 보여주냐 #저장하는거에 영향 X 밑에 보여주기 크기용 #아마도?
plt.imshow(array, interpolation="bilinear")
plt.show()#보여주기
fig.savefig('wordcloud.png') #파일이 저장되는 이름 ㅇㅇ



