## boj 2606 : 바이러스
> 문제 주소 : https://www.acmicpc.net/problem/2606
>
> 난이도 : silver 3

### 0. 문제
- 웜 바이러스는 네트워크를 통해 전파. 한 컴퓨터가 바이러스에 걸리면 연결된 모든 컴퓨터는 웜 바이러스에 걸린다.
- 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수는?

### 1. 문제 해결 방향
1. 연결된 모든 컴퓨터를 확인하는 것. 그래프
2. BFS와 DFS 모두 구현해보자!
3. 2차원 리스트를 구현해 경로를 저장한다.

### 2. 소스코드_DFS
- graph 2차원 리스트를 만들어 연결 정보를 저장한다.
- dfs를 구현한다. 현재 노드와 연결된 노드를 탐색하고, 재귀로 계속 타고 들어간다.
```python
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
```

### 3. 소스코드_BFS
- BFS를 구현한다.
- 현재 방문한 노드와 연결된 모든 노드를 탐색한다.
```python
# bfs 구현
def bfs(start, dic):
    queue = [start]
    while queue:
        for i in dic[queue.pop()]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
```

### 4. 느낀점
- 구현하기에는 DFS가 더 쉬운 것 같다.