import heapq
import sys
input = sys.stdin.readline
INF = float(1e9)

N, M, X = map(int,input().split())
graph = [[]for i in range(N+1)]


for i in range(M):
    a,b,cost = map(int, input().split())
    graph[a].append((b,cost))

def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    heapq.heappush(q, (0, start))
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

ans = 0
for i in range(1,N+1):
    go = dijkstra(i)
    back = dijkstra(X)
    ans = max(ans, go[X] + back[i])

print(ans)