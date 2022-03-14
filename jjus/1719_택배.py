import sys,heapq

input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
# (n+1) X (n+1) 그래프 생성 : undirected weighted graph
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    graph[n1].append([n2, w])
    graph[n2].append([n1, w])




def dijkstra(start):
    q = []
    result = [0] * (N + 1)
    distance = [INF] * (N+1)
    distance[start] = 0
    heapq.heappush(q,(0,start))

    while q:
        d, n = heapq.heappop(q)
        if distance[n] < d:
            continue

        for node,dis in graph[n]:
            cost = d + dis
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q,(cost,node))
                if n == start :
                    result[node] = node
                else: result[node] = result[n]

    my_print(result)


def my_print(result):
    for x in range(1, N + 1):
        if result[x] == 0:
            print("-", end=" ")
        else:
            print(result[x], end=" ")
    print()

for i in range(1, N + 1):
    dijkstra(i)  # 각 node 별로 dijkstra