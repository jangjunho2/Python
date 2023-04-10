# 계산된 결과를 메모 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수 재귀함수로 구현


def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1)+fibo(x-2)
    return d[x]


print(fibo(10))
print(fibo(20))
print(fibo(99))
