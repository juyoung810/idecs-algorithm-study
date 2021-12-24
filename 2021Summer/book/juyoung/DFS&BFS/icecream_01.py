N,M = map(int,input().split())
graph = []
visited = []
# 얼음 틀의 정보 입력 받기
for _ in range(N):
    graph.append(list(map(int,input())))
    # 방문 여부를 나타내는 list 생성
    visited.append( [False for _ in range(M)])

# 북 동 남 서
dr = [-1,0,1,0]
dc = [0,1,0,-1]


def dfs(graph, r, c, visited):
    # 시작하는 노드 방문 표시
    visited[r][c] = True
    #print((r,c) , end = ' ')
    turn_count = 0
    d = 0 # 북쪽 부터 둘러보기
    while True:
        # 상 하 좌 우 를 살펴보도록 한다.
        nr = r + dr[d]
        nc = c + dc[d]
        # 재귀의 종료 조건: 상하좌우를 다 살펴봐도 인접한 노드가 없는 경우
        if turn_count == 4: return
        # 그래프 내의 좌료로 이동한다면
        if nr >= 0 and nr < N and nc >= 0 and nc < M:
            # 해당 좌표를 확인해서 0이면서 방문되지 않았으면 재귀적으로 호출
            if graph[nr][nc] == 0 and not visited[nr][nc]:
                dfs(graph,nr,nc,visited)
        # 다음 방향으로 이동
        d = (d+1) % 4
        turn_count += 1

count = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and visited[i][j] == False:
            # dfs 호출되는 만큼 인접하지 않은 영역 있는 것 이므로
            count += 1
            dfs(graph,i,j,visited)


print()
print(count)
