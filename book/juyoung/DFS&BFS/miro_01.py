from collections import deque

N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

# 북 동 남 서 -> 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


# 최소 경로를 찾기 위해서는 BFS 사용
def bfs(graph, N, M):
    # dequeue 에 튜플을 넣는다.
    q = deque()
    q.append((0,0))
    # queue 가 빌 때 까지
    while len(q) != 0:
        r,c = q.popleft()
        # 상하좌우 인접한 방문하지 않은 노드 존재하는지 확인
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if graph[nr][nc] == 1:
                    # 해당 노드 까지의 최단 경로를 더해준다.
                    # 한 노드에 대한 인접 노드 들은 같은 최단 경로를 같게 된다.
                    # level은 최단 경로를 나타낸다.
                    graph[nr][nc] = graph[r][c] + 1
                    q.append((nr, nc))


bfs(graph, N, M)
print(graph[N-1][M-1])
