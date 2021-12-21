'''
< 인구 이동 >

N X N 크기의 땅이 있고, 땅은 1 X 1개의 칸으로 나누어져 있다.
각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다.
인접한 나라 사이에는 국경선이 존재한다.
모든 나라는 1x1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

< 인구 이동 방법 >
- 국경선을 공유하는 두 나라의 인구 차이가 l명 이상, r명 이하라면, 두 나라가 공유하는 국경선을 하루 동안 연다.
- 위 조건에 의해 열어야 하는 국경선이 모두 열렸다면 인구 이동을 시작
- 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 하루 동안 연합이라고 한다.
- 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수) 가 된다. 편의상 소수점 버림
- 연합을 해체하고, 모든 국경선을 닫는다.
더 이상 인구 이동이 없을 때까지 지속된다.

각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는가?

< 문제 해결 방향 >
인접한 노드를 확인한다. 인구수의 차이가 조건을 충족하면 연결 관계에 넣는다.
연결된 노드들의 인구 수를 갱신한다.
위 과정을 반복한다?

< 알게된 것 >
abs : 절대값 구하는 함수

'''

from collections import deque
# import sys
# input = sys.stdin.readline

# 땅의 크기(N), L, R 값 입력받기
n, l, r = map(int, input().split())

# 전체 나라의 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 방향 정보(북 서 남 동)
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 인구 이동이 일어나는 날
result = 0

# bfs를 이용해 생성된 연합을 구한다.
def bfs(i, j):
    q = deque()
    q.append([i, j])
    union = [[i, j]]
    # 큐가 빌 때까지 반복
    while q:
        x, y = q.popleft()
        # 현재 위치에서 네 방향으로 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않고 방문하지 않은 국가라면
            if 0 <= nx < n and 0 <= ny < 0 and visited[nx][ny] == 0:
                # 현재 국가와의 인구수 차이가 l이상 r 이하라면
                if l <= abs(graph[i][j] - graph[nx][ny]) <= r:
                    q.append([nx, ny])  # 탐색할 국가로 추가
                    visited[nx][ny] = 1 # 방문처리
                    union.append([nx, ny])  # 연합에 추가
    return union    # 연합 국가를 반환

while True:
    visited = [[0] * n for _ in range(n)]   # 방문여부 갱신
    state = False   # 종료 조건
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:  # 방문하지 않은 국가라면
                union = bfs(i, j)   # 연합 구하기
                # 연합이 존재한다면
                if len(union) >= 1:
                    state = True
                    # 인구이동 후 인구수 계산
                    population = sum(graph[x][y] for x, y in union) // len(union)
                    for x, y in union:  # 인구수 갱신
                        graph[x][y] = population
    # 연합이 존재하지 않으면 종료
    if not state:
        break
    # 인구수 갱신이 끝나면 하루 추가
    result += 1

print(result)