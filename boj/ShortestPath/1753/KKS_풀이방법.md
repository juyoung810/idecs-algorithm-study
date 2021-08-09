# boj 1753 : 최단경로 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1753
> 
> 난이도: gold 5

## 1.문제설명
- 방향그래프가 주어졌을 때 시작점에서 다른 모든정점으로의 최단경로를 구해보자
## 2. 문제 접근법 
- 책에 나온 개선된 다익스트라 알고리즘을 사용하면 될것 같다.
## 3.문제 해결 아이디어 or 핵심
- 우선순의 q를 이용해보자

## 4.특별히 참고할 사항


## 5.코드구현
``` python
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
k = int(input())
distance = [INF] * (v+1)
graph = [[] for i in range(v+1)]
#from/to/cost
for i in range(e):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

def dij(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] =cost
                heapq.heappush(q,(cost, i[0]))

dij(k)
for i in range(1,v+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

```