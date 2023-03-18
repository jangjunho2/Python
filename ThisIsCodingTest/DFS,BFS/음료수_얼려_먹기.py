# 음료수 얼려먹기


# dfs 정의

'''
find_crack
(0)얼음 틈을 찾는 함수 (왼쪽위부터 찾음)
#(1)칸막이 or 방문한거 visited True 확인하기. 방문한 얼음이면 continue
틈이 있는 경우 dfs함수 호출 >> 틈 찾기 이어서 진행... 한번 만 돌면 됨
'''


def find_crack():
    global ice
    for i in range(row):  # 여기서 row를 사용 할수 있는 이유??? 지역변수아님?
        for j in range(col):
            # 틈(0) and not 방문한곳이면  #dfs 함수 호출
            if array[i][j] == 0 and not visited[i][j]:
                dfs(array, i, j)
                ice += 1


'''
dfs함수
상하좌우를 스택에 담음 #단, 담을수 없는 경우: (1) 칸막이 or 존재 하지 않는 좌표면 무시함
스택에 있는 것들을 방문 #visited true해주기
이어진 모든칸을 방문했으면  #ice++ #얘는 find_crack함수에서?
>> 다시 틈찾기 이어서 진행...
'''


def dfs(array, r, c):
    visited[r][c] = True
    drow = [1, -1, 0, 0]  # 상하좌우
    dcol = [0, 0, -1, 1]  # 상하좌우
    for i in range(4):
        nrow = r+drow[i]
        ncol = c+dcol[i]
        if 0 <= nrow < row and 0 <= ncol < col:  # 좌표 안에 있다면?
            # 틈(0) and not 방문한곳이면  #dfs 함수 호출 (재귀함수 ))
            if array[nrow][ncol] == 0 and not visited[nrow][ncol]:
                dfs(array, nrow, ncol)  # 방문 ㄱ

    # n, m 입력받기
row, col = map(int, input().split())

# 방향정의

# 얼음 생성  # (0)은 얼음  (1)은 칸막이
array = [list(map(int, input())) for _ in range(row)]
# print(array)

visited = [[False]*col for _ in range(row)]  # 얼음 크기만큼 방문한곳 기록
# print(visited)
ice = 0  # 아이스크림 수

find_crack()  # dfs 호출함수시작
print(ice)  # 정답 출력
