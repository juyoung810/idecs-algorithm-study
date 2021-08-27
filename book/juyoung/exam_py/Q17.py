
# K의 최대 크기는 1000

import sys
from collections import deque

input = sys.stdin.readline

# 이동 방향 설정
# 상 하 좌 우
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

# N,K 입력 받기
n, k = map(int, input().split())

# N * N 크기의 보드 생성
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# s, x, y 입력 받기
s, x, y = map(int, input().split())
q = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            q.append((board[i][j],i,j,0)) # 시간은 모두 0 으로 초기화

# 작은 순 update위해 정렬
q.sort()
q = deque(q)


while q:
    virus,nr,nc,time = q.popleft()
    if time == s:
        break
    else:
        for i in range(4):
            lr = nr + dr[i]
            lc = nc + dc[i]
            if 0<=lr<n and 0<=lc<n:
                if board[lr][lc] == 0:
                    board[lr][lc] = virus
                    q.append((virus,lr,lc,time+1)) # time +1 초에 변경 되었음을 의미
# # 바이러스 리스트 생성
# virus = [[] for _ in range(k + 1)]
# # 해당 바이러스의 종류의 idx에 바이러스 좌표 더하기
# for i in range(n):
#     for j in range(n):
#         virus[board[i][j]].append([i, j])
#


#
# # s초 만큼 bfs 실시
# q = deque()
# # q에 집어 넣기
# for i in range(1, k + 1):
#     q.extend(virus[i])
# for _ in range(s):
#     length = len(q)
#     for i in range(length):
#         nr, nc = q.popleft()
#         for j in range(4):
#             lr = dr[j] + nr
#             lc = dc[j] + nc
#             if 0 <= lr < n and 0 <= lc < n:
#                 if board[lr][lc] == 0:
#                     board[lr][lc] = board[nr][nc]
#                     # virus[board[lr][lc]].append([lr,lc])
#                     q.append([lr, lc])
#
print(board[x - 1][y - 1])
