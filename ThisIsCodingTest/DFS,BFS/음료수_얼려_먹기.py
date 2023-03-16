# 음료수 얼려먹기


# dfs 정의

'''
(0)얼음 틈을 찾는 함수 (왼쪽위부터 찾음)
#(1)칸막이 or (0)방문한거 visited True 확인하기. 방문한 얼음이면 패스
틈이 있는 경우 dfs함수 호출 >> 틈 찾기 이어서 진행... 한번 만 돌면 됨

dfs함수
상하좌우를 스택에 담음 #단, 담을수 없는 경우: (1) 칸막이 or 존재 하지 않는 좌표면 무시함
스택에 있는 것들을 방문 #visited true해주기
이어진 모든칸을 방문했으면  #ice++
>> 다시 틈찾기 이어서 진행...
'''


def dfs(array, visited):
    pass  # 구현 끝나면 지울것
    ice = 0  # 아이스크림 수


def 틈을찾는함수():
    pass

    # n, m 입력받기
n, m = map(int, input().split())

# 방향정의
direction = [0, 1, 2, 3]  # 상하좌우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


# 얼음 생성  # (0)은 얼음  (1)은 칸막이
array = [list(map(int, input())) for _ in range(n)]
# print(array)

visited = [[False]*n]*m  # 얼음 크기만큼 방문한곳 기록

dfs(array, visited)
