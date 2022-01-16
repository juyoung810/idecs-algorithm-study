from collections import deque
import sys
input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(E):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = set()
def bfs(graph, start):
    queue = deque([start])
    while queue:
        curNode = queue.popleft()
        for node in graph[curNode]:
            if node not in visited:
                queue.append(node)
                visited.add(node)

cnt = 0
for i in range(1,N+1):
    if i not in visited:
        bfs(graph, i)
        visited.add(i)
        cnt += 1

print(cnt)