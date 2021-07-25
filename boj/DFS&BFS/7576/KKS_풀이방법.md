# boj 7576: 토마토
> 문제 주소: https://www.acmicpc.net/problem/7576

# 문제 해결 방향
결과
- 탐색을 진행하고 모든 토마토가 다 익었으면 날짜를 출력해야함 
- 안익은 토마토가 남았으면 -1 출력
- 토마토가 처음부터 다 익어있었으면 0출력

# 처음에 실수한 부분
1. bfs함수를 2차원배열을 단순 순회하면서 진행함 -> 익은 토마토가 여러개 있는 경우 결과가 다름

# 해결하기 위해서
1. 큐를 만들고 2차원 배열을 순회하며 익은 토마토가 있는경우 queue에 추가해줌

#### BFS -> 주변으로 퍼져나가면서 탐색 (최단 날짜이기 때문에 BFS 사용)

#### 1. BFS함수 정의 (입력 생략)
```python
BFS 함수 정의
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

```

#### 2. BFS 함수에 토마토 위치 제공하기 위한 단계
```python
queue = deque()
for x in range(n):
    for y in range(m):
        if graph[x][y] == 1:
            queue.append((x,y))
```

#### 3. 함수실행
``` python
bfs()
```

#### 4. 결과출력
개인적으로 이부분이 생각보다 힘들었음.
1. 일단 bfs코드 진행 후에 0인 토마토를 찾아봐야함 -> 존재하면 -1출력
2. 애초에 토마토가 없었을 경우 (전부 -1인 경우) -> 0 출력
3. 일단 토마토가 들어있으면 result - 1출력
``` python
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
elif result == -1: #전부 -1인경우(토마토가 없는경우)
    print(0)
else:
    print(result -1) #토마토가 있긴 한 경우 만약에 다 익어있어도 0 result가 1되서 0이 출력
```