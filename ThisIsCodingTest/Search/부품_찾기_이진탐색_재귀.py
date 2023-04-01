def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)


n = int(input())
have = list(map(int, input().split()))
m = input()
wants = list(map(int, input().split()))


have.sort()

for want in wants:
    result = binary_search(have, want, 0, n-1)
    if result == None:
        print("no", end=" ")
    else:
        print("yes", end=" ")
