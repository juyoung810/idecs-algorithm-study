from collections import deque
N = int(input())
K = int(input())
graph = [[] for i in range(N+1)]
for i in range(K):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

visited = set()

def bfs(start, graph, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if node not in visited:
                queue.append(node)
                visited.add(node)

bfs(1, graph, visited)
print(len(visited) - 1)
