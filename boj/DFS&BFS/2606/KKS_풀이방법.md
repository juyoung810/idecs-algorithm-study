### boj 2606: 바이러스
> 문제주소 : https://www.acmicpc.net/problem/2606

### 문제 해결 방향
1. 시작점은 첫번째 컴퓨터임
2. 그래프는 양방향 그래프

### 처음에 실수한점
1. 양방향그래프인데 연결 정보를 단방향으로 받았음

#### 이웃한 컴퓨터로 퍼져나가니깐 BFS

### 코드구현
## 1. 양방향 연결정보 처리

``` python
from collections import deque
n = int(input())
k = int(input())
connection_info = [[] for i in range(n+1)]
for i in range(k):
    n1, n2 = map(int, input().split())
    connection_info[n1].append(n2)
    connection_info[n2].append(n1)
```
## 2. 방문한 노드 처리
책에서는 노드 갯수만큼 False담은 리스트만들어서 방문하면 True로 만들어주지만
개인적으로 set을 쓰는게 더 편하고 기능도 더 많은듯...
```python
visited = set()
```

## 3. bfs 함수 구현
```python
def bfs(graph, start, visited):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                queue.append(i)
                visited.add(i)
```

## 4. 함수실행과 결과 출력
마지막에 방문한 곳이 즉 바이러스가 방문하여 감염시킨곳인데 1은 원래 걸렸으니 한개 빼줘서 출력!
``` python
bfs(connection_info, 1, visited)
print(len(visited)-1) 
```