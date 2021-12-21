from collections import deque
N, K = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))
S, X, Y = map(int, input().split())

virus = []

time = 0
for i in range(N):
    for j in range(N):
        if graph[i][j] != 0:
            virus.append((graph[i][j],i,j,time))
virus.sort()
q = deque(virus)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while q:
    virus,x,y, time =q.popleft()
    if time == S:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx < N and 0<= ny < N:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,nx,ny,time+1))

print(graph[X-1][Y-1])