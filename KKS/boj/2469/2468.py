from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    _temp = list(map(int, input().split()))
    graph.append(_temp)

max_val = max(map(max, graph))
min_val = min(map(min, graph))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, depth):
    queue = deque()
    queue.append((x,y))
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if graph[nx][ny] >= depth:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))


safe_area = 0
for depth in range(min_val,max_val+1):
    visited = [[0] * N for _ in range(N)]
    _temp = 0

    for x in range(N):
        for y in range(N):
            if visited[x][y] == 0 and graph[x][y] >= depth:
                bfs(x, y, depth)
                _temp += 1
    if _temp > safe_area:
        safe_area = _temp
print(safe_area)

