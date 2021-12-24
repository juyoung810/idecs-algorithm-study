# boj 7576: 토마토
> 문제 주소: https://www.acmicpc.net/problem/7576


# 문제 해결 방향
조건
1. 토마토가 모두 0 일 경우 -> -1 출력
2. 토마토가 모두 0은 아니지만, 탐색 후 0으로 남아있는 경우 -> -1 출력
3. 토마토가 모두 1인 경우 -> 0 출력
4. 여러개의 1이 존재할 수 있다. -> BFS의 시작점이 여러개이므로 동시에 시작할 수 있도록 해야한다.

#### 최단 날짜를 구한다 -> BFS 
1. BFS의 시작지점 알기 위해 토마토를 순회하며 익은 토마토를 Queue에 더한다.
-> 이때 익은 토마토의 갯수가 0 인 경우 모든 토마토가 익지 못하는 경우 이므로 -1 이다.
```python
q = deque()
for i in range(N):
    for j in range(M):
        # 익은 토마토 q에 더한다
        if tomatoes[i][j] == 1:
            q.append((i, j))

if len(q) == 0:
    print(-1)
```
2. BFS를 동시에 시작할 수 있도록 BFS 에 queue를 넘겨 실행한다.
상하좌우를 확인하며 익지 않은 토마토일 경우 해당 토마토 위치의 visited를 이동 전 vistied 거리에서 +1 더한다(level 표시)
그리고 익은 토마토로 표시한 후 queue에 더한다.
```python
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

```   
3. 가장 visited가 큰 것을 찾는다. 동시에 BFS를 했음에도 0이 남아있는 경우를 찾는다.
```python
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

    if not isTomato:
        print(day)
    else:
        print(-1)
```
이때, 모두 1인 경우 BFS 결과 visited 가 모두 0 이므로 0이 출력된다.