arr = [0]*1000001

n = int(input())

for i in input().split():
    arr[int(i)] = 1

m = int(input())

for i in input().split():
    if arr[int(i)] == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
