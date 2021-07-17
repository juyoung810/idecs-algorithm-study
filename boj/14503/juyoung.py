
# 북 동 남 서
dr = [-1,0,1,0]
dc = [0,1,0,-1]

# N * M 크기 방
N,M = map(int, input().split())
# r, c , direction
r, c , direction = map(int,input().split())
board = []
for i in range(N):
    board.append([int(x) for x in input().split()])

#print(board)
# 전체 청소 상태 0 으로 초기화
state = [[0]*M for _ in range(N)]
# 처음위치 청소하기
state[r][c] = 1
turn_count = 0
room_count = 1
while True:
    # 왼쪽 방향 회전
    direction = (direction - 1 + 4) % 4
    nr = r + dr[direction]
    nc = c + dc[direction]
    # 회전한 뱡향이 방이고, 청소 안했을 경우
    if board[nr][nc] == 0 and state[nr][nc] == 0:
        r = nr
        c = nc
        state[r][c] = 1
        room_count += 1
        turn_count = 0
    else:
        turn_count += 1
    # 4번 회전했을 때
    if turn_count == 4:
        # 후진
        nr = r - dr[direction]
        nc = c - dc[direction]
        if board[nr][nc] == 0:
            r = nr
            c = nc
        else:
            break
        turn_count = 0

    #print(state)


print(room_count)