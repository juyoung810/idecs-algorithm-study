# 플루이드- 워샬 알고리즘 이용
# 거리 1000 이하인 노드 전부 연결


import sys

input = sys.stdin.readline
INF = int(1e9)
# test 개수 입력 받기
t = int(input())

def find_edge(distance,graph):
    # 전체를 돌면서, 거리 1000 이하이면 간선 연결
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                graph[i][j] = 0
            elif (abs((distance[j][0] - distance[i][0])) + abs((distance[j][1] - distance[i][1]))) <= 1000:
                graph[i][j] = 1


def path(graph):
    # 플루이드 워샬 알고리즘 수행하며, 처음과 페스티벌 연결되었는지 확인
    for k in range(n + 2):
        for a in range(n + 2):
            for b in range(n + 2):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for _ in range(t):
    # 편의점의 개수 입력받기
    n = int(input())

    distance = []
    for i in range(0, n + 2):
        x, y = map(int, input().split())
        distance.append((x, y))

    graph = [[INF] * (n + 2) for _ in range(n + 2)]




    find_edge(distance,graph)
    path(graph)





    if graph[0][n + 1] != INF:
        print("happy")
    else:
        print("sad")
