import copy
from collections import deque
n = int(input())
k = int(input())

queue = deque()
visited = set()

for i in range(k):
    queue.append(tuple(map(int, input().split())))
queue = deque(sorted(queue, key = lambda x : x[0]))
_tmp = copy.deepcopy(queue)
for item in _tmp:
    x, y = item
    queue.append((y,x))

visited.add(1)
while queue:
    node1, node2 = queue.popleft()
    if node1 in visited:
        visited.add(node2)

print(len(visited)-1)