from collections import deque
# m : 가로, n: 세로
m, n = map(int, input().split())
graph = []
#정보 입력받음 -> 1은 익은토마토, 0은 안익은 토마토, -1은 토마토 없음
for i in range(n):
    graph.append(list(map(int,input().split())))

#상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny <m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

queue = deque()
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            queue.append((x,y))

bfs()

result = -2
isTrue = False
print(graph)
for row in graph:
    for element in row:
        if element == 0:
            isTrue = True
        result = max(result, element)
        print(result)
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result -1)
