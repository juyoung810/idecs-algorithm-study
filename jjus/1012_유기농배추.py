# 몇 묶음인지 찾기 -> BFS 횟수로 찾기
import sys

input = sys.stdin.readline


def bfs(x, y):
    # 북 동 남 서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    q = list()
    visited[x][y] = True
    q.append((x, y))

    while q:
        now_x, now_y = q.pop(0)
        for i in range(4):
            nx = dx[i] + now_x
            ny = dy[i] + now_y
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny))


T = int(input())

while T != 0:
    M, N, K = map(int, input().split())

    cabbage = list()
    board = [[0] * M for _ in range(N)]  # Y: 0 - N-1
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        y,x = map(int, input().split())
        board[x][y] = 1
        cabbage.append((x, y))

    count = 0
    for x, y in cabbage:
        if not visited[x][y]:
            bfs(x, y)
            count += 1

    print(count)
    T -= 1
