# 이진탐색
# 배열이 정렬 되어있어야만 사용 가능
# 시간복잡도 O(logN)
# 절반씩 데이터가 줄어들도록 만든다는 점에서 퀵 정렬과 공통점이 있음
# 재귀 or 반복문으로 구현 가능

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)


# n(원소의 개수)와 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)

'''
입력 예시: 
10 7
1 3 5 7 9 11 13 15 17 19
출력 예시:
4
'''
