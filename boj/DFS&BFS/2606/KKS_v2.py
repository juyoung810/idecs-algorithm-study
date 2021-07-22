from collections import deque
n = int(input())
k = int(input())
connection_info = [[] for i in range(n+1)]
for i in range(k):
    n1, n2 = map(int, input().split())
    connection_info[n1].append(n2)
    connection_info[n2].append(n1)

visited = set()
def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.add(i)

bfs(connection_info, 1, visited)
print(len(visited)-1)