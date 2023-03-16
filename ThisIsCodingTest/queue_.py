from collections import deque

quque = deque()

quque.append(1)
quque.append(2)
quque.popleft()
quque.append(3)
quque.append(4)
quque.popleft()
quque.append(5)


print(quque)
quque.reverse()
print(quque)
