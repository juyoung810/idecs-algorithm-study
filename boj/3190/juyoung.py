# 북 동 남 서
# x : 행
# y : 열
dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

# 보드의 크기 N*N
N = int(input())
board = [[0] * N for _ in range(N)]

# 사과 위치
for _ in range((int(input()))):
    r,c = map(int, input().split())
    # 0행 부터 시작 설정 # 행 열
    board[r - 1 ][c - 1] = 1

directions = []
# 이동 위치 받기
for _ in range((int(input()))):
    directions.append(list(input().split()))

con = 0
# 동쪽(오른쪽 부터 시작)
d = 1
# 뱀 처음 위치
# 뱀 처음 몸의 길이
head = [0, 0]
bam = []
bam.append([0,0])
time_count = 0
state = True
while state:
    if len(directions) != 0 :
        direction = directions.pop(0)
    else:
        direction[0] = str(N*N)
        direction[1] = "T"
    while time_count < int(direction[0]):
        time_count += 1
        # 시작 오른쪽  = 동쪽
        nr = head[0] + dr[d]
        nc = head[1] + dc[d]
        # 벽과 부딪히면 종료
        if nc < 0 or nc >= N or nr < 0 or nr >= N:
            state = False
            break
        # 자기 자신의 몸과 부딪히면 종료
        elif [nr, nc] in bam:
            state = False
            break
        # 머리 먼저 이동
        head[0] = nr
        head[1] = nc
        bam.append([nr,nc])
        # 사과 존재하지 않으면 꼬리 움직인다.
        if board[nr][nc] == 0:
            bam.pop(0)
        # 사과가 존재하는 경우 해당 사과 지운다
        else:
            board[nr][nc] = 0
    if direction[1] == 'D':
        d = (d + 1) % 4
    elif direction[1] == 'L':
        d = (d - 1 + 4) % 4
    else: continue
    #print(d)


print(time_count)
