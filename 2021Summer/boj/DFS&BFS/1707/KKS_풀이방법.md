### boj 1707: 이분그래프
> 문제주소 : https://www.acmicpc.net/problem/1707

문제풀이 이전에 이분그래프의 개념을 이해해야 했음..
![alt text]https://www.google.com/url?sa=i&url=https%3A%2F%2Fwoovictory.github.io%2F2020%2F01%2F26%2FBipartite-Graph%2F&psig=AOvVaw01syv14JFATScMsnIatAij&ust=1627199294486000&source=images&cd=vfe&ved=0CAoQjRxqFwoTCPDNn_Gb-_ECFQAAAAAdAAAAABAI

뭐 대충 이런게 이분그래프임 색을 2개만 써서 노드를 색칠한다고 했을때 자신과 인접한 노드들과 다른색으로 칠해져야함

### 문제해결방안
- 색을 2개 써서 색칠을 해보자 (0방문안함, 방문함: 1 or -1)
- 인접한 노드들과 다른색으로 칠해져야함 -> 인접함 -> BFS사용

### 처음에 실수한 점
- 색칠하는 함수를 만들고, 검사하는 함수를 따로 만들어서 체크하려고 했으나 시간초과 out
    -> 색칠과 동시에 검사를 해야함

### 코드구현
## 1. 필요정보 입력받기
```python
from collections import deque
import sys
input = sys.stdin.readline
k = int(input())
```
## 2. 연결정보 입력받기
여기서 연결정보를 관리하는 graph를 만들고
색의 정보를 관리하는 color를 만듬
```python
for i in range(k):
    vertex, edge = map(int, input().split())
    isTrue = True
    graph = [[] for i in range(vertex+1)]
    color = [0 for i in range(vertex+1)]
    for j in range(edge):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    for y in range(1, vertex+1): #노드를 순회하면서 노드를 bfs함수에 넣을지 결정
        if color[y] == 0: #만약에 해당노드가 아직 색칠이 안됐으면
            if not bfs(y): #bfs함수에 넣고 true / False값을 받음 만약에 False가 return 되면
                isTrue = False
                break
    print("YES" if isTrue else "No") #isTrue가 여전히 true면 yes 아니면 no
```

## 3. 색칠과 검사 동시에 하는 BFS함수 만들기
```python
def bfs(start):
    color[start] = 1 #입력으로 들어온 노드를 색칠함
    queue = deque()
    queue.append(start) #시작점 큐에 밀어넣고 bfs탐색시작
    while queue:
        v = queue.popleft()
        for node in graph[v]: #팝된 노드의 인접 노드들 살펴봄
            if color[node] == 0:  #아직 색칠이 안됐다면
                color[node] = -color[v] #-붙혀서 다른색으로 색칠해주고
                queue.append(node)#큐에 넣음
            else: #색칠이 됐는데...
                if color[node] == color[v]: #팝된 노드랑 색이 같다?
                    return False #false 리턴함
    return True
```
