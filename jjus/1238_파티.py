import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

distance = [INF] * (N+1)


for _ in range(M):
    n1,n2,c = map(int,input().split())
    graph[n1].append([n2,c])



def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start))
    distance = [INF] * (N + 1)
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for n,d in graph[node]:
            cost = dist + d
            if distance[n] > cost:
                distance[n] = cost
                heapq.heappush(q,(cost,n))
    return distance

# 갈떼
r = 0
for i in range(1,N+1):
   go = dijkstra(i)[X]
   back = dijkstra(X)[i]
   r = max(r,go+back)

print(r)



