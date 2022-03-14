import sys, heapq

input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2, d = map(int, input().split())
    graph[n1].append([n2, d])
    graph[n2].append([n1, d])

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    distance = [INF] * (N + 1)
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] < dist:
            continue

        for n, d in graph[node]:
            cost = dist + d
            if cost < distance[n]:
                distance[n] = cost
                heapq.heappush(q, (cost, n))
    return distance


d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)

ans = min(d1[v1] + d2[v2] + d3[N], d1[v2] + d3[v1] + d2[N])

if ans >= INF:
    print(-1)
else:
    print(ans)
