from collections import deque

# N * M 토마토 박스 입력 받는다.
M, N = map(int, input().split())

# 토마토의 정보를 입력 받는다.
tomatoes = []
for i in range(N):
    tomatoes.append(list(map(int, input().split())))

# tomatoes 가 익는데 걸리는 날짜 계산
visited = [list(0 for _ in range(M)) for _ in range(N)]

# 상 하 좌 우 확인
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def BFS(q):
    while len(q) != 0:
        r, c = q.popleft()
        # 상 하 좌 우 확인
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M:
                # 익지 않은 토마토일 경우 q에 더한다.
                if tomatoes[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    # 익은 토마토로 변경
                    tomatoes[nr][nc] = 1
                    # print(nr,nc,visited[nr][nc])
                    q.append((nr, nc))


q = deque()
isNoOne = True
for i in range(N):
    for j in range(M):
        # 익은 토마토 q에 더한다
        if tomatoes[i][j] == 1:
            q.append((i, j))
# 모두 1이 아닌 경우 == 모두 익지 못하는 경우
if len(q) == 0 :
    print(-1)

else:
    # 시작 노드가 여러개 일 수 있다. 동시에 시작할 수 있도록 queue 자체를 넘긴다.
    BFS(q)
    isTomato = False
    # BFS 실행 이후 전체 익지 못하는 상황인지 확인
    day = visited[0][0]
    for i in range(N):
        for j in range(M):
            if visited[i][j] > day:
                day = visited[i][j]
            if tomatoes[i][j] == 0:
                isTomato = True
                break
    # 모두 1인 경우는 어차피 다 0 이다.
    if not isTomato:
        print(day)
    else:
        print(-1)
