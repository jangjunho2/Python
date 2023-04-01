n, m = map(int, input().split())  # n=세로,m=가로
x, y, dir = map(int, input().split())

# 방문위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0]*m for _ in range(n)]
d[x][y] = 1  # 현재 좌표 방문 처리
# 맵 생성
array = [(list(map(int, input().split()))) for _ in range(n)]  # 바다(1) 땅(0)

# print(array)

dx = [0, 1, 0, -1]  # 북동남서 0 1 2 3
dy = [1, 0, -1, 0]  # 북동남서
# 북>서>남>동  ->0 > 3 > 2 > 1


# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1:
        dir = 3


count = 1  # 방문한 칸의 횟수
turn_time = 0

# 시뮬 시작
while True:
    # 왼쪽회전
    turn_left()
    # 앞 에칸 좌표 계산
    nx = x+dx[dir]
    ny = y+dy[dir]
    # 가보지 않은 칸이 앞에있다면 이동
    if array[nx][ny] == 0 and d[nx][ny] == 0:
        x, y = nx, ny
        turn_time = 0
        count += 1
        d[x][y] = 1
        continue
    else:  # 앞으로 갈수 없는 경우
        turn_time += 1
        if turn_time == 4:  # 네방향 전부 못가는 경우
            nx = x-dx[dir]  # 뒤로 한걸음 계산
            ny = y-dy[dir]
            # 바라보는 방향유지 뒤로한칸 이동
            if array[nx][ny] == 0:  # 뒤가 땅이다
                x, y = nx, ny
                turn_time = 0
            else:  # 뒤가 바다인 경우
                break  # 이동 종료
        else:    # 네 번 미만 회전인 경우 continue
            continue
print(count)
