# 순차탐색
# 파이썬의 내장함수 count() 는 순차탐색을 이용
# 최악의 경우 시간 복잡도 O(N)

def sequential_search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i+1


array = list(input().replace(" ", ""))  # 문자열 입력
target = input()  # 찾을 문자 입력

print(sequential_search(array, target))
