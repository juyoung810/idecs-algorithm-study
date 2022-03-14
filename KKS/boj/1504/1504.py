import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]


for i in range(E):
    a,b,cost = map(int,input().split())
    graph[a].append((b,cost))
    graph[b].append((a,cost))

v1, v2 = map(int,input().split())
start = 1

def dijkstra(start):
    q = []
    distance = [INF] * (V + 1)
    heapq.heappush(q,(0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

case1 = dijkstra(1)[v1] + dijkstra(v1)[v2]+ dijkstra(v2)[V]
case2 = dijkstra(1)[v2] + dijkstra(v2)[v1]+ dijkstra(v1)[V]

if case1 >= INF and case2 >= INF:
    print(-1)
else:
    print(min(case1, case2))