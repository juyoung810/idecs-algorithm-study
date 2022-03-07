"""
적록 색약인 경우 / 아닌 경우 나눠서 bfs 두 번
"""
import sys

input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(input().rstrip()))
ㅌ
visited = [[False] * N for _ in range(N)]
# 동 서 남 북
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


# state 0: 아님
# state 1: 맞음
def bfs(x, y, state):
    q = []
    q.append([x, y])
    while q:
        now_x, now_y = q.pop()
        visited[now_x][now_y] = True
        for d in range(4):
            nx = now_x + dx[d]
            ny = now_y + dy[d]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    if state == 1:
                        if board[nx][ny] == board[now_x][now_y]:
                            q.append([nx, ny])
                        elif board[now_x][now_y] == 'R' and board[nx][ny] == 'G':
                            q.append([nx, ny])
                        elif board[now_x][now_y] == 'G' and board[nx][ny] == 'R':
                            q.append([nx, ny])
                    else:
                        if board[nx][ny] == board[now_x][now_y]:
                            q.append([nx, ny])


not_red = 0
red = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 0)
            not_red += 1
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, 1)
            red += 1

print(not_red, red)
