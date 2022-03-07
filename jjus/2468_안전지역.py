import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, std):
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
                    if board[nx][ny] > std:  # 기준 보다 클 경우
                        q.append([nx, ny])


max_h = max(max(board))
now_h = 1 # 아무것도 잠기지 않았을 경우
count = 0
for i in range(1,max_h):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            if not visited[j][k] and board[j][k] > i:
                bfs(j,k,i)
                count += 1
                #print(count)
    if now_h < count:
        now_h = count

print(now_h)


