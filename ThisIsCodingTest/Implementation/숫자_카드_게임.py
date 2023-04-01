import sys

input = sys.stdin.readline

row, col = map(int, input().split())

nums = [min(map(int, input().split())) for _ in range(row)]

print(max(nums))
