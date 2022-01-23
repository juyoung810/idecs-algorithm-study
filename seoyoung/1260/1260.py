'''
< DFS와 BFS >
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램 작성.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문, 더 이상 방문할 수 있는 점이 없는 경우 종료

< 아이디어 >
1. 정점 번호가 작은 것을 먼저 방문하는 방법? min을 사용해서 append하기
2. dfs는 깊이우선탐색. 재귀로 구현
3. bfs는 너비우선탐색. 큐를 이용해 구현
'''

def dfs(v, graph):
    print(v, end=' ')
    for i in graph[v]:
        if i not in visited:
            visited.append(i)
            dfs(i, graph)

def bfs(v, graph):
    queue = deque([v])
    while queue:
        print(queue[0], end=' ')
        for i in graph[queue.popleft()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

import sys
input = sys.stdin.readline
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for i in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for line in graph:
    line.sort()

visited = [v]
dfs(v, graph)
print()
visited = [v]
bfs(v, graph)
