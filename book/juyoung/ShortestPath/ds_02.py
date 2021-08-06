# 전보
# 특정 도시 -> 모든 도시
# 다익스트라
# N = 30,000 -> 힙으로 리스트 구현

import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,c = map(int,input().split())

# 간선의 정보 저장 위해
graph =  [[] for _ in range(n+1)]
# 최단 거리 저장 위해
distance = [INF] * (n+1)

# 모든 간선의 정보 입력 받는다.
for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

# 다익스트라 함수
def dijkstra(start):
    q = []
    # 시작부분 처리
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q: # 큐가 비지 않을 때 까지
        dist,now = heapq.heappop(q)
        if dist < distance[now]: # 이미 처리된 적 있으면
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count +=1
        max_distance = max(max_distance,d)

print(count-1,max_distance)

