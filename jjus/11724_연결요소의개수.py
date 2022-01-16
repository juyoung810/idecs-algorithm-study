'''
bfs 통해서 몇 묶음이 존재하는지 찾기 -> 812ms
'''
import sys
input = sys.stdin.readline


def bfs(start):
    q = list()
    visited[start] = True
    q.append(start)
    while q:
        now = q.pop(0)
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True
                q.append(n)


N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)

count = 0
for i in range(1,N+1):
    if not visited[i]:
        bfs(i)
        count +=1

print(count)
