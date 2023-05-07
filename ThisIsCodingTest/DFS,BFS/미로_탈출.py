# https://www.acmicpc.net/problem/2178

import sys
from collections import deque

input = sys.stdin.readline


def bfs(maze, row, col, start_depth, dst):
    queue = deque([[row, col, start_depth]])
    visited[row][col] = True
    # 상하좌우
    drow = [1, -1, 0, 0]
    dcol = [0, 0, -1, 1]

    while queue:
        # print(queue)
        v = queue.popleft()
        temp = 0
        for i in range(4):
            nrow = v[0]+drow[i]
            ncol = v[1]+dcol[i]
            depth = v[2]
            if 0 <= nrow < n and 0 <= ncol < m:  # 범위 내 이고
                # 방문한적없는 곳 and 방문가능한 1일떄 방문
                if not visited[nrow][ncol] and maze[nrow][ncol] == 1:
                    queue.append([nrow, ncol, depth+1])
                    visited[nrow][ncol] = True
                    # 좌표가 목적지이면 종료
                    if [nrow, ncol] == dst:
                        print(depth+1)
                        return


n, m = list(map(int, input().split()))

maze = []
for i in range(n):
    maze.append(list(map(int, input().rstrip())))

visited = [[False]*m for _ in range(n)]

dst = [n-1, m-1]  # 목적지 좌표

bfs(maze, 0, 0, 1, dst)
