input_data = input()

steps = [[2, 1], [2, -1],
         [-2, 1], [-2, -1],
         [1, -2], [1, 2],
         [-1, 2], [-1, -2]]


row = input_data[1]
col = input_data[0]

col = ord(col)-ord('a')+1  # a,b,c좌표를 1,2,3숫자로 만듬

count = 0

for step in steps:
    nrow, ncol = int(row), col
    nrow += step[1]
    ncol += step[0]

    if 1 > nrow or 1 > ncol or 8 < ncol or 8 < nrow:  # 이동 불가능하면 넘어감
        continue

    count += 1  # 가능한 경우라면 count++

print(count)
