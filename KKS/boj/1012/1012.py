import sys
from collections import deque
input = sys.stdin.readline
# 상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
#graph[x][y] -> x는 위 아래 움직임, y는 좌 우 움직임
def bfs(graph,x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y =queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))

T = int(input())
for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    # M 가로 ,N = 세로
    graph = [[0] * M for _ in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    for x in range(N): #세로
        for y in range(M): #가로
            if graph[x][y] == 1:
                bfs(graph, x, y)
                graph[x][y] = 0
                cnt += 1
    print(cnt)



