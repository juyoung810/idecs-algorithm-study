import sys

input = sys.stdin.readline
INF = int(1e9)
N, M = map(int, input().split())
# (n+1) X (n+1) 그래프 생성 : undirected weighted graph
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    graph[n1].append([n2, w])
    graph[n2].append([n1, w])

visited = [False] * (N + 1)  # 방문 처리 기록용
distance = [INF] * (N + 1)  # 거리 테이블용
result = [0] * (N + 1)  # 가장 먼저 거쳐가야하는 노드 번호 저장


def my_print():
    for x in range(1, N + 1):
        if result[x] == 0:
            print("-", end=" ")
        else:
            print(result[x], end=" ")
    print()


# 방문하지 않은 노드 && 시작 노드와 최단 거리 노드
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, N + 1):
        if not visited[i] and distance[i] < min_value:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드 -> 시작 노드 거리 계산 및 방문 처리
    distance[start] = 0
    visited[start] = True
    # 시작노드와 인접한 노드들에 대해 최단 거리 계산
    for i in graph[start]:
        distance[i[0]] = i[1]
        result[i[0]] = i[0] # 안접 노드의 경우 최초 방문 노드가 자기 자신

    # 시작 노드 제외한 N-1개의 노드에 도착하는 최단 거리 계산
    for _ in range(N - 1):
        now = get_smallest_node()  # 방문 x 이면서 시작 노드와 최단 거리인 노드 반환
        visited[now] = True
        for next in graph[now]:
            cost = distance[now] + next[1]
            if cost < distance[next[0]]: # 이미 저장된 경로보다 더 짧은 경로일 경우
                distance[next[0]] = cost # cost 업데이트
                result[next[0]] = result[now] # 최초 방무 노드 업데이트


for i in range(1, N + 1):
    dijkstra(i)  # 각 node 별로 dijkstra
    my_print()
    visited = [False] * (N + 1)  # 방문 처리 기록용
    distance = [INF] * (N + 1)  # 거리 테이블용
    result = [0] * (N + 1)  # 가장 먼저 거쳐가야하는 노드 번호 저장