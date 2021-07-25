from collections import deque
n, m = map(int, input().split())
map_info = []
for i in range(n):
    map_info.append(list(map(int, input())))
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if map_info[nx][ny] == 0:
                continue
            if map_info[nx][ny] == 1:
                queue.append((nx, ny))
                map_info[nx][ny] = map_info[x][y] + 1
    return map_info[n-1][m-1]

print(bfs(0,0))




