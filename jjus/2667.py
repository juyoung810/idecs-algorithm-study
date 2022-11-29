import sys
input = sys.stdin.readline

# N * N 좌표
N = int(input())

# graph 초기화 선언
graph = []
for _ in range(N):
    graph.append(list(input().rstrip())) # 0 : 집 없음, 1 : 집 있음

visited = [[0] * N for _ in range(N)] # 방문 확인 함수

# 동 서 남 북
dx = [1 ,-1 ,0 ,0]
dy = [0 ,0 ,-1 ,1]
result = []


def bfs(s):
    q = []
    cx,cy = s
    visited[cx][cy] = 1
    q.append([cx,cy])
    count = 0
    while q:
        cx, cy = q.pop(0)
        count += 1
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] == 0 and graph[nx][ny] == '1':
                    visited[nx][ny] = 1
                    q.append([nx, ny])

    return count


for x in range(N):
    for y in range(N):
        if visited[x][y] == 0 and graph[x][y] == '1':
            result.append(bfs([x,y]))

result.sort()
print(len(result))
for i in range(len(result)):
    print(result[i])


