# boj 1260 DFS와BFS
> sivler 2
> 
> https://www.acmicpc.net/problem/1260


# 1. 문제 설명
- DFS 결과, BFS 결과 출력하기
- 방문 가능한 정점 여러 개일 경우 정점 번호 작은 것 부터 방문

# 2. 문제 해결 방향
- 방향이 없는 그래프 생성
- 정점 번호 작은 순 방문하기 위해 오름차순 정렬
- DFS 실행 -> visited 초기화 -> BFS 실행

# 3. 소스코드

- N+1개의 노드의 연결 정보 저장위해 N+1개의 row 가지는 배열 생성
- 방향이 없는 그래프이므로 두 정점 모두에 연결 정보 추가
```python
N,M,V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
```

- 작은 번호 순 방문 위해 각 node의 연결 정보 정렬
```python
for i in range(1,N+1):
    graph[i].sort()
```
- visited 정보 초기화 -> DFS -> visited 초기화 -> BFS
```python
visited = [False] * (N+1)
dfs(graph, visited, V)
print()
bfs(graph,V)

```
- DFS 함수
```python
def dfs(graph,visited, start):
    print(start, end = " ")
    visited[start] = True
    for n in graph[start]:
        if not visited[n]:
            dfs(graph, visited,n)
```
- BFS 함수
```python
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
```

# 4. 시간 복잡도 - 84ms
- 함수로 만들어서 호출하는 경우가 더 빠름
- 정렬 : 모두 연결된 경우 최대 V*O(NlogN)
- BFS와 DFS 시간 복잡도 : O(V+E) 

