# boj 1766 : 문제집 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1766
> 
> 난이도: gold2

## 1.문제설명
- N개의 문제를 풀 예정
- 먼저 푸는 것이 좋은 문제가 있는 문제는 먼저 풀어야함
- 가능하면 쉬운 문제부터 풀어야함 ( 중요 )
## 2. 문제 접근법 
- 기존의 위상정렬에서는 차수가 같은 노드들에 대해서는 다양한 순서가 발생할 수 있었음
- 하지만 여기서는 차수가 같은 경우에도 노드의 크기가 작은 순서대로 풀길 원함
## 3.문제 해결 아이디어 or 핵심
- 처음에 deque를 사용해서 deque에 넣기전에 정렬을 한번 하고 넣어봄 -> 실패
- 매 순서마다 가장 크기가 작은 노드를 찾아야함 -> min heap 사용
## 4.특별히 참고할 사항
- min heap을 모르면 못풀었을 것..
- 다양한 문제를 경험해보는게 좋음

## 5.코드구현
``` python
import sys
import heapq
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
indegree = [0] * (N+1)

for item in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = []
    result = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:
        now = heapq.heappop(q)
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q, i)

    for i in result:
        print(i, end = " ")

topology_sort()

```