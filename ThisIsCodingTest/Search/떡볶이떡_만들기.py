def binary_search(array, total, start, end):
    while start <= end:
        mid = (start+end)//2
        temp = 0
        for i in range(len(array)):
            if array[i] > mid:
                temp += array[i]-mid
        if total > temp:  # 손님이 주문한 양 > 만든 떡의 양 # 양이 부족한 경우 # 왼쪽 부분 탐색
            end = mid-1
        else:               # 손님이 주문한 양 <= 만든떡의 양 # 양이 많은 경우 # 오른쪽 부분 탐색
            result = mid
            start = mid+1
    return result


n, m = map(int, input().split())  # 떡의 갯수,총 길이
rice_cake = list(map(int, input().split()))
rice_cake.sort()


result = binary_search(rice_cake, 6, 1, max(rice_cake))

print(result)
