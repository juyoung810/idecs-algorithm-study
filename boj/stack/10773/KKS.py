from collections import deque
queue = deque()
n = int(input())
for i in range(n):
    _temp = int(input())
    if _temp == 0:
        queue.pop()
    else:
        queue.append(_temp)
print(sum(queue))