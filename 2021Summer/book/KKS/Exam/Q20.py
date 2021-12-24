import copy
from itertools import combinations

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().split()))

teacher = []
empty = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'T':
            teacher.append((i, j))
        elif graph[i][j] == 'X':
            empty.append((i, j))


# 빈곳 3개 조합 만들기
# 순회하면서 graph deepcopy해서 벽 설치하고 시뮬레이션

def check():
    for t in teacher:
        x, y = t
        # 상 하 좌 우
        nx, ny = x, y
        while nx > 0:
            nx -= 1
            if graph_[nx][ny] == "S":
                return False
            if graph_[nx][ny] == "O":
                break

        nx, ny = x, y
        while nx < N - 1:
            nx += 1
            if graph_[nx][ny] == "S":
                return False
            if graph_[nx][ny] == "O":
                break

        nx, ny = x, y
        while ny > 0:
            ny -= 1
            if graph_[nx][ny] == "S":
                return False
            if graph_[nx][ny] == "O":
                break

        nx, ny = x, y
        while ny < N - 1:
            ny += 1
            if graph_[nx][ny] == "S":
                return False
            if graph_[nx][ny] == "O":
                break
    return True


empty_comb = list(combinations(empty, 3))
for comb in empty_comb:
    graph_ = copy.deepcopy(graph)
    graph_[comb[0][0]][comb[0][1]] = 'O'
    graph_[comb[1][0]][comb[1][1]] = 'O'
    graph_[comb[2][0]][comb[2][1]] = 'O'
    if check():
        print("YES")
        break
else:
    print("NO")
