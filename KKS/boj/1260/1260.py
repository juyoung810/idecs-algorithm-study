from collections import deque
V, E, start = map(int,input().split())
graph = [[] for i in range(V+1)]

for _ in range(E):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)
for item in graph:
    item.sort()


def BFS(graph, start):
    visited = set()
    visited.add(start)
    queue = deque([start])
    while queue:
        curnode = queue.popleft()
        print(curnode, end=' ')
        for nextnode in graph[curnode]:
            if nextnode not in visited:
                queue.append(nextnode)
                visited.add(nextnode)


visited = set()
def DFS(graph, start, visited):
    visited.add(start)
    print(start, end = ' ')
    for nextnode in graph[start]:
        if nextnode not in visited:
            DFS(graph, nextnode, visited)


DFS(graph, start, visited)
print()
BFS(graph, start)
