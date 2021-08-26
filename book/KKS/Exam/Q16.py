import copy
from itertools import combinations

N, M = map(int, input().split())

graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

# 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    graph_[x][y] = 2

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
            continue
        if graph_[nx][ny] != 0:
            continue
        else:
            dfs(nx, ny)


virus = []
zeros = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            virus.append([i, j])
        elif graph[i][j] == 0:
            zeros.append([i, j])

zeros_comb = combinations(zeros, 3)
safety_zone_list = []
for case in zeros_comb:
    graph_ = copy.deepcopy(graph)

    graph_[case[0][0]][case[0][1]] = 1
    graph_[case[1][0]][case[1][1]] = 1
    graph_[case[2][0]][case[2][1]] = 1

    for v in virus:
        dfs(v[0], v[1])

    safety_zone = 0
    for row in range(N):
        for col in range(M):
            if graph_[row][col] == 0:
                safety_zone += 1
    safety_zone_list.append(safety_zone)

print(max(safety_zone_list))
