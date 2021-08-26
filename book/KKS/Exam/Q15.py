import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = int(input())
graph = [[] * N]
INF = int(1e9)
distance = [[INF] * N]
distance[X] = 0

for _ in range(M):
    n1, n2 = int(input().split())
    graph[n1].append(n2)

q = deque([X])
while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == INF:
            distance[next] = distance[now] + 1
            q.append(next)

if K not in distance:
    print(-1)

for i in range(distance):
    if distance[i] == K:
        print(distance[i])

