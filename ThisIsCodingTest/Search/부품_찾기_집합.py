# 파이썬 set는 내부적으로 해시 테이블을 사용하므로 값의 존재 여부를 확인하는 연산의 시간 복잡도는 O(1) 입니다.
n = int(input())
have = list(map(int, input().split()))
m = input()
wants = list(map(int, input().split()))
