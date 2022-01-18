'''
< 연결 요소의 개수 >
방향 없는 그래프가 주어졌을 때,연결 요소의 개수를 구하는 프로그램을 작성하시오

< 아이디어 >
1. dfs를 통해 구현한다.
2. 정점들에 대해 방문여부를 확인후, 방문하지 않은 정점이면 cnt를 하나 추가하고 dfs로 연결된 정점을 확인한다.
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
visited = [False] * (n+1)
cnt = 0

graph = [[] for i in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(graph, start, visited):
    visited[start] = True

    for node in graph[start]:
        if visited[node] == False:
            dfs(graph, node, visited)

for i in range(1, n+1):
    if visited[i] == False:
        cnt += 1
        dfs(graph, i, visited)

print(cnt)