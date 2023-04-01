# 스택 구현
stack = []

stack.append(1)
stack.append(2)
stack.pop()
stack.append(3)
stack.append(4)
stack.pop()
stack.append(5)


print(stack)  # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소 출력
