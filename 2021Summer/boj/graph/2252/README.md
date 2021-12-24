# boj 2252 : 줄 세우기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/2252
> 
> 난이도: gold 2

## 1.문제설명
- n명의 학생들 키순으로 줄을 세우려고함
- 두 학생의 키를 비교해서 줄을 세우려고함
## 2. 문제 접근법 
- 전형적인 위상정렬 문제
## 3.문제 해결 아이디어 or 핵심
- 책의 위상정렬 그대로 구현하면됨

## 4.특별히 참고할 사항


## 5.코드구현
``` python
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    q = deque()
    result = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=" ")

topology_sort()

```