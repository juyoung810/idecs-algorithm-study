# 서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수 있다.
# V의 갯수가 20000 개 이상이므로 heap를 통해 최단 경로를 저장한다.
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())

distance = [INF] * (n + 1)

# graph = [[0] * (n+1) for _ in range(n + 1)]
graph = [[] for _ in range(n+1)]

start = int(input())

for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))


def dijkstra(start):
    # 힙 생성
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # q가 비지 않을 때 까지
        dist, now = heapq.heappop(q)
        if distance[now] < dist:  # now가 이미 처리된 적 있을 경우
            continue
        for i in graph[now]:  # i 는 now-> i
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)

for d in range(1, n + 1):
    if distance[d] == INF:
        print('INF')
    else:
        print(distance[d])
