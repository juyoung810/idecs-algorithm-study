# 특정 거리의 도시 찾기
# N개의 도시(1~N), M개의 단방향 도로 존재, 모든 도로의 거리는 1
# 인접 리스트 그래프 형성
# x->x는 항상 0
# x -> 모든 도시 : 최단 거리 K인 것 출력
# 최단 거리 -> BFS 탐색

import sys
from collections import deque

input = sys.stdin.readline

# n : 도시개수, m: 도로 개수, k: 거리 정보, x: 출발 도시
n, m, k, x = map(int, input().split())

# 인접리스트
graph = [[] for _ in range(n + 1)]  # 1 ~ n 까지의 index 사용 위해
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)  # 단방향 그래프


# 최단 거리 구하기 위해 bfs
# bfs -> deque 사용
def bfs(graph, start):
    # 방문 확인 위한 리스트
    distance = [-1] * (n + 1)
    distance[start] = 0
    q = deque([start])
    while q:
        now = q.popleft()
        for city in graph[now]:
            if distance[city] == -1:  # 방문하지 않았을 경우
                distance[city] = distance[now] + 1  # level 표시
                q.append(city)

    return distance


result = bfs(graph, x)
check = True
for i in range(1,len(result)):
    if result[i] == k:
        print(i,end = " ")
        check = False

if check:
    print(-1)

