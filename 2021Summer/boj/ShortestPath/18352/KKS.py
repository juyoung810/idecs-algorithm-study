import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

ans = []
def dij():
    q = []
    heapq.heappush(q, (0,x))
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node in graph[now]:
            cost = dist + 1
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

dij()

for idx in range(n+1):
    if distance[idx] == k:
        print(idx)
if k not in distance:
    print(-1)
