import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

count = (m//(k+1))*k
count += m % (k+1)

result = 0

result += count*data[-1]
result += (m-count)*data[-2]

print(result)
