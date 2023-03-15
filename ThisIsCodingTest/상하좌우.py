import sys


def check(x, y):
    if [x, y] in mat:
        return True


def L(x, y):
    cur_x, cur_y = x, y
    x -= 1
    if check(x, y):
        return x, y
    else:
        return cur_x, cur_y


def R(x, y):
    cur_x, cur_y = x, y
    x += 1
    if check(x, y):
        return x, y
    else:
        return cur_x, cur_y


def U(x, y):
    cur_x, cur_y = x, y
    y += 1
    if check(x, y):
        return x, y
    else:
        return cur_x, cur_y


def D(x, y):
    cur_x, cur_y = x, y
    y -= 1
    if check(x, y):
        return x, y
    else:
        return cur_x, cur_y


dic = {"L": L, "R": R, "U": U, "D": D}

dx = 1
dy = 1

n = int(sys.stdin.readline())

# 맵 만들기
mat = [[i, j] for i in range(1, n+1) for j in range(1, n+1)]

# 이동 방향 받기
btns = sys.stdin.readline().split()

for btn in btns:
    dx, dy = dic[btn](dx, dy)

print(dx, dy)
