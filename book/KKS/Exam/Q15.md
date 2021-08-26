# boj 18352 : 특정거리의 도시찾기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/18352
> 
> 난이도: silver 2

## 1.문제설명
- 어떤 나라에서 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다
- 이때 도로의 거리는 1
- 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시중 최단거리가 K인 모든 도시들의 번호를 출력해라

## 2. 문제 접근법 
- N,M이 너무 커서 플로이드 와샬은 안됨
- heapq이용한 다익스트라로 풀어보자
## 3.문제 해결 아이디어 or 핵심
- 기존의 다익스트라 문제에서는 거리마다 가중치가 있지만
- 여기선 그냥 1로 고정

## 4.특별히 참고할 사항
- 기존의 다익스트라로 풀어도 되긴하지만...
- 가중치가 모두 1이면 bfs로 풀어도 된다고한다..

## 5.코드구현
``` python
import sys
from collections import deque
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
distance[x] = 0

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == INF:
            distance[next_node] = distance[now] + 1
            q.append(next_node)

for i in range(n+1):
    if distance[i] == k:
        print(i)

if k not in distance:
    print(-1)
```