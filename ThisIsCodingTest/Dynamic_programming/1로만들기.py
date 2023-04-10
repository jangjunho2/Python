# 완전탐색(최적화) 풀이
# 탑다운방식 O
#  DP X

counts = [float('inf')]


def to_one(n, count):
    if min(counts) <= count:
        return
    if n == 1:
        counts.append(count)
        return
    count += 1
    if n % 5 == 0:
        to_one(n/5, count)
    if n % 3 == 0:
        to_one(n/3, count)
    if n % 2 == 0:
        to_one(n/2, count)
    to_one(n-1, count)


n = int(input())
count = 0
to_one(n, count)
print(counts)
print(min(counts))
