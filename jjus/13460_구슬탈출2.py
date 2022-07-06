import sys
from collections import deque
input = sys.stdin.readline

# board 생성
N,M = map(int,input().split())

board = []
for i in range(N):
    board.append(list(input().rstrip()))
    for j in range(M):
        if board[i][j] == "R":
            rx, ry = i,j # red
        elif board[i][j] == 'B':
            bx,by = i,j # blue
# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfd(rx,ry,bx,by) :
    q = deque()
    q.append((rx,ry,bx,by))
    visited = []
    visited.append((rx,ry,bx,by))
    count = 0
    while q:
        for _ in range(len(q)):
            rx,ry,bx,by = q.popleft()
            if count > 10:
                print(-1) # 움직인 횟수 10회 초과일 경우 -1
                return
            if graph[rx][ry] == '0':
                print(count)
                return
            for i in range(4):
                nrx, nry = rx,ry
                # 빨간 공
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if graph[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if graph[nrx][nry] == '0':
                        break
                nbx, nby = bx,by
                while True:
                    nbx += dx[i]
                    nby += dy[i]
                    if graph[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if graph[nbx][nby] == '0':
                        break
                if graph[nbx][nby] == '0': # 파란 구슬이 먼저 구멍 or 동시면 무시
                    continue
                if nrx == nbx and nry == nby:
                    

