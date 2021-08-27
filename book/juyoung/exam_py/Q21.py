# 인구 이동
# 국경선 공유하는 두 나라의 인구차이 L이상, R 이하면 국경선 연다
# 국경선 열리면 인구이동 시작 -> 연합이라고 부름
# 연합 이루고 있는 각 칸의 인구수 = (연합으 인구수)/(연합을 이루고 있는 칸의 개수) - 소수점 버림
# 연합 해체 후 국경선 모두 닫는다.

# 인구 이동 몇 번 발생하는지 구하기

# bfs 실시 후 인구 이동 -> dfs 몇 번 실시되는지 파악

import sys
from collections import deque

input = sys.stdin.readline


def bfs(r, c):
    q = deque()
    group = []
    sum_num = board[r][c]
    count = 1
    q.append((r, c))
    group.append((r, c))
    visited[r][c] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if (nr, nc) not in group and visited[nr][nc] == 0:
                    if L <= abs(board[r][c] - board[nr][nc]) <= R:
                        group.append((nr, nc))
                        sum_num += board[nr][nc]
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                        count += 1

    return sum_num//count , count, group


def update_board():
    for i in range(len(group)):
        for r,c in group[i]:
            board[r][c] = sum_list[i]

# n,l,r 입력 받기
n, L, R = map(int, input().split())

# board 생성
board = []
# 상 하 좌 우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
for _ in range(n):
    board.append(list(map(int, input().split())))

# board에 대해 dfs 실시
move = 0
visited = [[0] * n for _ in range(n)]
while True:
    group = []
    sum_list = []
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                sum_num,count,temp = bfs(i, j)
                if count > 1: # 연합 국가 존재하면
                    group.append(temp)
                    sum_list.append(sum_num)
    if len(group) == 0:
        break
    update_board()
    move += 1
    visited = [[0] * n for _ in range(n)]

print(move)
