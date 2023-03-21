n = int(input())

array = [[a, int(b)] for a, b in ((input().split())for _ in range(n))]
array.sort(key=lambda x: x[1])

for i in range(n):
    print(array[i][0], end=" ")
