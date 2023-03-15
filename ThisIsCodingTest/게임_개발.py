n, m = map(int, input().split())  # n=세로,m=가로
x, y, dir = map(int, input().split())

block_visited = 1  # 방문한 칸의 갯수


# 맵 생성
game_map = [(list(map(int, input().split()))) for _ in range(n)]
original_map = game_map  # 맵 원본 땅(0), 바다(1)

print(game_map)

dx = [0, 1, 0, -1]  # 북동남서
dy = [1, 0, -1, 0]  # 북동남서
dir_types = [0, 1, 2, 3]  # 0:북 1:동 2:남 3:서

'''
1.현재 위치에서 현재 방향을 기준으로 왼쪽 방향 (반시계 방향으로 90도 회전한 방향 )부터 차례대로 갈곳을 정한다

2.캐릭터의 바로 왼쪽 방향에 가보지 않은 칸이 존재한다면,왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
  왼쪽 방향에 가보지 않은 칸이 없다면,왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다

3.만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다.
  단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.

'''

stop = False
while not stop:
    # 3번 조건이 만족하면 끝나게
    blocked = 0  # 주변의 가본 곳 or 바다의 수
    for i in dir_types:  # 막힌 주변수 검사
        if [x+dx[i], y+dy[i]] == 1:
            blocked += 1
            if blocked == 4:  # 4곳 전부 막힌 경우 방향유지하고 뒤로 한걸음
                for i in range(len(dir_types)):
                    if dir == dir_types[i]:
                        nx = x-dx[i]
                        ny = y-dy[i]

                        if original_map[nx][ny]:  # 뒤가 바다라면
                            stop = True
                        else:
                            x, y = nx, ny  # 이동

    dir = (dir+3) % 4  # 왼쪽으로 회전
    for i in range(len(dir_types)):
        if dir == dir_types[i]:
            nx = x+dx[i]
            ny = y+dy[i]

        if game_map[nx][ny] == 1:  # 바다(1) or 방문한 경우(1) 인 경우
            continue  # 2번 구현

        x, y = nx, ny  # 이동
        block_visited += 1  # 방문한 칸 횟수++
        game_map[nx][ny] = 1  # 방문 한곳은 다시 방문하지 않으므로 바다(1) 처리


print(block_visited)
