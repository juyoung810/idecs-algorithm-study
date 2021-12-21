# N * N 보드
# 사과 주어짐
# 처음에 오른쪽 향하고, 초 마다 이동
# 사과 먹으면 몸길이 증가
# 벽에 부딪히거나, 자기 자신의 몸에 부딪히면 종료
# X D -> X 초 뒤 오른쪽으로 회전
# X L -> X 초 뒤 왼쪽으로 회전

# 보드의 크기 입력 받기
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
# (n+1) * (n+1) 크기의 보드 생성
board = [[0] * (n+1) for _ in range(n+1)]
# 사과 갯수 입력, 배치
m = int(input())
for _ in range(m):
    r,c = map(int,input().split())
    board[r][c] = 1

# 북 동 남,서
# 오른쪽 회전 = +1
# 왼쪽 회전 = -1
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# 이동 입력 받기
directions = []
for _ in range(int(input())):
    directions.append(list(input().rstrip().split()))
print(directions)


# 뱀의 몸
head = [1,1]
bam = deque([[1,1]]) # 들어가는게 머리, 나오는게 꼬리
# 동쪽부터 시작
d = 1
# 시간 count
time_count = 0
state = True

while state:
    if len(directions) != 0:
        direction = directions.pop(0)
    else:
        direction[0] = str(n*n-time_count)
        direction[1] = 'T'
    print(direction)
    while time_count < int(direction[0]):
        time_count += 1
        # 시작 오른쪽 = 동쪽
        nr = head[0] + dr[d]
        nc = head[1] + dc[d]
        # 이동했을때 벽에 부딪히거나, 몸에 부딪힌 경우 중단
        if nr < 1 or nr > n or nc < 1 or nc > n:
            state = False
            break
        elif [nr,nc] in bam:
            state = False
            break
        # 부딪히지 않은 경우 사과 존재 유무 판별
        else:
            bam.append([nr, nc])
            head = [nr,nc]
            if board[nr][nc] == 1: # 사과존재하는경우
                board[nr][nc] = 0
            else:
                bam.popleft() # 꼬리 이동
        print(bam)
    # 방향 전환
    if direction[1] == 'D':
        d = (d+1) % 4
    elif direction[1] == 'L':
        d = (d - 1 + 4) % 4

print(time_count)