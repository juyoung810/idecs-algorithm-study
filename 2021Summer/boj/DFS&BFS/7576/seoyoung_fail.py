### 토마토
## 토마토는 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관
## 하루가 지나면 익지 않은 토마토들은 익은 토마토들의 영향을 받아 익게 된다.
## 며칠이 지나면 토마토들이 다 익게 되는지 알고싶다.
## 상자의 일부 칸에는 토마토가 들어있지 않을 수도 있다.

# bfs를 사용할 것!
from collections import deque
import numpy as np

n, m = map(int, input().split())

# 토마토가 든 상자의 정보를 받는다.
box = []
for i in range(n):
    row = list(map(int, input().split()))
    box.append(row)

# 익은 토마토가 들어있는 위치를 찾아 리스트에 저장한다. 저장된 위치를 각각 시작으로!
ripe = []

n_idx = 0
for line in box:
    idx = line.index(1)
    ripe.append((n_idx, idx))
    n_idx += 1

# 이동할 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# bfs 구현하기
def bfs(x, y):
    tomatoes = [[0 for i in range(m)] for k in range(n)]
    queue = deque()
    queue.append((x,y))
    # 시작 노드를 익은 토마토로 표시
    tomatoes[x][y] = 1
    # 큐가 빌 때까지 반복
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nx = r + dx[i]
            ny = c + dy[i]
            # 박스를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 토마토 없으면 무시
            if tomatoes[nx][ny] == -1:
                continue
            # 안 익은 토마토 만나면
            if tomatoes[nx][ny] == 0:
                # 익는 데까지 걸린 날짜 구해야 함
                tomatoes[nx][ny] = tomatoes[x][y] + 1
                # 방문한 노드 추가
                queue.append((nx, ny))
    return tomatoes

result = bfs(ripe[0][0], ripe[0][1])
result = np.concatenate(result).tolist()

if len(ripe) != 1:
    for start in ripe:
        compare = bfs(start[0],start[1])
        compare = np.concatenate(compare).tolist()
        for i in range(len(compare)):
            if compare[i] < result[i]:
                result[i] = compare[i]

if -1 in result:
    date = -1
else:
    date = max(result)
print(date)