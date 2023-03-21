n, k = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()  # 오름차순 정렬
arr2.sort(reverse=True)  # 내림차순 정렬

# arr1의 앞(작은수)에 arr2의 앞(큰수) 대입


# arr1 i <arr2 i ? 바꿈 : 안바꿈
# 바꿧다면 i++하면서 계속 이어서 진행
# 안바꿧다면 바로 break
for i in range(k):
    if arr1[i] < arr2[i]:
        arr1[i], arr2[i] = arr2[i], arr1[i]
    else:
        break

# print(arr1)
print(sum(arr1))
