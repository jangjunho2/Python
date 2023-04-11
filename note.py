# n 개의 False 값을 갖는 리스트를 만들고, 그 리스트를 m 개 복사하는 것을 의미합니다.
# 그러므로 visited 리스트의 각 행은 동일한 리스트 객체를 참조합니다.
# 이렇게 되면 visited[0][0] = True와 같이 한 행의 값을 변경하면, 다른 모든 행의 해당 인덱스 값도 동시에 변경되는 문제가 발생합니다.
# n, m = 4, 5
# visited = [[False]*n]*m
# visited[0][0] = True
# visited[0][1] = True
# visited[0][2] = True
# visited[0][3] = True
# print(visited)


# [False]*10은 10개의 False 값을 갖는 리스트를 만듭니다. 이때 각 값은 서로 다른 메모리 위치에 저장된 별개의 객체입니다.
# visited = [False]*10
# visited[1] = True
# print(visited)


# 불변 객체이면서 지역변수인 a는 값을 조회하는 수준에서는 global을 쓰지않고도 함수에서 이용할수있다?
# def print_a():
#     # a += 1
#     print(a)
#     for i in range(a):
#         print(i)
# a = 10
# print_a()


# 불변객체라서 값을 바꾼게아니라 재할당 하는거임
# a = 1
# a += 1
# print(a)


# 불변객체라서 값을 바꾼게아니라 재할당 하는거임
# a = "hello"
# a += " world"
# print(a)


# list 정렬 방법
# a = [1, 4, 2]
# a.sort()
# print(a)


# join함수 이용은 str만가능하다
# a=[1,2,3,4,5]
# b=['1','2','3','4','5']
# # res="".join(a)
# res=" ".join(b)
# print(res)


# join함수 이용법
# sen="avc"
# sen=list(sen)
# sen[1]='b'
# sen=' '.join(sen)
# print(sen)

# join함수 이용법 (int로 구성된 리스트  map을 이용해 str로 바꾼후 출력)
# nums=[0,1,2,3,4,5]
# print(" ".join(map(str,nums)))

# 람마함수 선언 방법
# lambda x : x * 2

'''
Python에서 기본적으로 지원하는 정렬 알고리즘은 Tim Sort는 Stable 합니다.
(Tim sort는 Insertion Sort와 Merge Sort를 Hybrid 하여 구현한 알고리즘으로 Insertion과 Merge 모두 Stable Sort Algorithm 입니다.)
동일한 값을 갖는 경우 순서가 보장되는 Stable Algorithm이니 그냥 나이 순으로 정렬하기만 해도 됩니다.
'''
# 리스트 언패킹
# def print_numbers(a, b, c):
#     print(a)
#     print(b)
#     print(c)
# x = [10, 20, 30]
# print_numbers(*x)

# join 쓸때 양옆에 도 넣고싶으면? #언패킹 이용
# abc = "abc"
# abc_with_commas = ",".join(["", *abc, ""])
# print(abc_with_commas)

# 해싱 할땐 소수를 사용하여 해시값 생성하면 충동 가능성 -- ex)31

# 잘못된 리스트 복사
# a,b모두 같은 리스트를 참조하고 있기 때문에 둘다 [10,10]
# a = [10]
# b = a
# b.append(10)
# print(a, b)

# 리스트 복사
# 1. 슬라이싱을 통한 방법
# a = [1, 2, 3]
# b = a[:]
# b.append(10)
# print(a, b)
# 2. copy() 메스드를 이용한 리스트 복사
# a = [1, 2, 3]
# b = a.copy()
# b.append(10)
# print(a, b)

# 반복문에서 iterator 값을 수정해도 바뀌지않는다.
# for i in range(100):
#     print(i)
#     if i == 50:
#         i -= 1

# 리스트에서 원소를 제거하면서 반복문을 돌리면, 리스트의 크기가 줄어들기 때문에 반복문이 예상대로 동작하지 않을 수 있다.
# a = [1, 2, 3, 4, 5]
# for i in a:
#     if i == 2:
#         a.remove(i)
#     print(i)
