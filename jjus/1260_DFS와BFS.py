"""
단순 정렬 후 bfs, dfs

84ms

"""
import sys
input = sys.stdin.readline


def dfs(graph,visited, start):
    print(start, end = " ")
    visited[start] = True
    for n in graph[start]:
        if not visited[n]:
            dfs(graph, visited,n)


def bfs(graph, start):
    visited = [False] * (N + 1)
    q = []
    visited[start] = True
    q.append(start)

    while q:
        now = q.pop(0)
        print(now, end = " ")
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True
                q.append(n)



N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,N+1):
    graph[i].sort()

visited = [False] * (N+1)
dfs(graph, visited, V)
print()
bfs(graph,V)
