'''
< 특정 거리의 도시 찾기 >

dfs : 깊이 우선 탐색 알고리즘. 그래프 탐색. 최대한 멀리 있는 노드를 우선으로 탐색. 스택 자료구조 이용
bfs : 너비 우선 탐색 알고리즘. 가까운 노드부터 탐색. 선입선출 방식 큐를 이용해 효과적으로 구현 가능. 인접한 노드를 반복적으로 큐에 넣기

< 문제 >
- 1~N번까지의 도시와 M개의 단방향 도로가 존재. 모든 도로의 거리는 1.
- 특정한 도시 x로부터 출발해 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 k인 모든 도시의 번호를 출력하는 프로그램을 작성하라.

< 문제 해결 방향 >
bfs를 이용한다. 가까운 노드부터 탐색하여, 최단거리를 계산하고 k에 해당하면 답에 추가한다.
방문 여부를 표시하는 배열을 만들고, 그래프의 연결 정보를 받는다.
시작 노드와 연결된 도시들을 큐에 집어넣고, 도시를 방문할 때마다 방문여부를 갱신하고 최단거리를 계산한다.
최단거리가 k에 해당하면 답에 추가한다.
'''

import sys
from collections import deque
input = sys.stdin.readline

# 도시의 개수 n, 도로의 개수 m,  거리 정보 k, 출발 도시의 번호 x
n, m, k, x = map(int, input().split())
# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 그래프의 연결 정보를 받는다.
graph = [[] for _ in range(n+1)]
# A 도시에서 B 도시로 이동하는 단방향 통로 존재.
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# bfs 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시를 확인
    for nxt in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[nxt] == -1:
            distance[nxt] = distance[now] + 1
            q.append(nxt)

check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

# 만일 최단 거리가 k인 도시가 없다면 -1 출력
if check == False:
    print(-1)