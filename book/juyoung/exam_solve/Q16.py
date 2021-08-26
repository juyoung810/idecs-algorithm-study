# 연구소
# 0 : 빈칸, 1 : 벽, 2: 바이러스
# 바이러스가 있는 곳 상하좌우 인접한 빈칸 퍼져 나갈 수 있다.
# 새로 세울 수 있는 벽의 개수는 3개
# 바이러스가 퍼질 수 없는 안전한 영역의 최댓값 구하기

# 3 <= N, M <= 8
# 벽의 갯수는 2보다 크거나 같고, 10보다 작거나 같은 자연 수
# 빈칸 갯수 3개 이상

# 0 나올 때 마다 벽 세우고 BFS -> 탐색 결과 저장
# 가장 적은 탐색 결과가 답
import copy
import sys
from collections import deque

input = sys.stdin.readline

# 상하좌우로 움직이기 위해
# 북동남서
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
# 결과 저장 위해
max_safe = 0


# bfs 해서 감염되지 않은 곳 찾기
def bfs(temp, spread, not_safe):
    global max_safe
    # bfs 위한 queue
    while spread:
        start = spread.pop(0)
        for i in range(4):
            tr = dr[i] + start[0]
            tc = dc[i] + start[1]
            if 0 <= tr < n and 0 <= tc < m:
                if temp[tr][tc] == 0:
                    temp[tr][tc] = 2
                    not_safe += 1
                    spread.append((tr, tc))

    max_safe = max(max_safe, n * m - (not_safe + 3))  # 3은 새로 세운 벽의 수


# 벽 세개 세우기 -> 세운 벽 갯수 세서 3개면 BFS 하고, 다시 벽 허물기
def wall(cnt,r,c,not_safe):
    if cnt == 3:
        temp = copy.deepcopy(board)
        spread = copy.deepcopy(virus)
        bfs(temp, spread, not_safe)
        return

    for i in range(r,n):
        for j in range(c,m):
            if board[i][j] == 0:
                board[i][j] = 1
                wall(cnt + 1,i,j+1,not_safe)  # 재귀적으로 벽 세우기 때문에 이미 세웠던 곳에 다시 세울 일 없다.
                board[i][j] = 0  # 벽 다시 허물기
        # 처음에 돌 때만 startColumn 보다 큰 경우 부터 돈다.
        c = 0

# 지도의 가로 세로 크기
n, m = map(int, input().split())

# n * m 크기의 지도 생성
board = []  # 0으로 초기화

# 입력 받기
for _ in range(n):
    board.append(list(map(int, input().rstrip().split())))

# 바이러스 리스트 생성
virus = []
# 0이 아닌 곳 count
not_safe = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        if board[i][j] != 0:
            not_safe += 1

wall(0,0,0,not_safe)
print(max_safe)
