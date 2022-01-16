'''
웜 바이러스는 네트워크를 통해 전파. 한 컴퓨터가 바이러스에 걸리면 연결된 모든 컴퓨터는 웜 바이러스에 걸린다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수는?

< 아이디어 >
1. 연결된 모든 컴퓨터를 확인하는 것. 그래프
2. BFS와 DFS 모두 구현해보자!
3. 2차원 리스트를 구현해 경로를 저장한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for i in range(n+1)]
for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 구현
def dfs(start, dic):
    for i in dic[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, dic)

visited = []
dfs(1, graph)
print(len(visited)-1)


# bfs 구현
def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

visited = []
bfs(1, graph)
print(len(visited)-1)