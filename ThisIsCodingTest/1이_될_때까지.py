n, k = map(int, input().split())

cnt = 0

while True:
    if n < k:              # n이 k보다 작아서 더 이상 나눌 수 없으면 반복문을 종료합니다.
        break

    target = (n // k) * k  # k의 배수를 찾습니다.
    cnt += n - target      # k의 배수로 빼는 경우와 그렇지 않은 경우를 한 번에 계산합니다.
    n = target

    cnt += 1               # k로 나누는 연산을 수행합니다.
    n //= k

cnt += (n - 1)
print(cnt)
