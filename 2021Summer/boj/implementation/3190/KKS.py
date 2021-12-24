from collections import deque
#입력 & 초기값 세팅
n = int(input()) # 보드의 길이
k = int(input()) # 사과의 갯수

#사과 좌표 받기
apple_loc = []
for _ in range(k):
    apple_loc.append(list(map(int,input().split())))

#방향전환 정보 받기
l = int(input())
movement_change = {}
for _ in range(l):
    x, c = input().split()
    movement_change[int(x)] = c

#맵 데이터 설정(사과위치1,안가본 곳 0)
map_data = [[0] * n for _ in range(n)]
for loc in apple_loc: #사과 좌표는 1로
    x, y = loc
    map_data[x-1][y-1] = 1

def direction_change(direction_c):
    global direction
    if direction_c == "D":
        direction += 1
        if direction > 3:
            direction = 0
    else:
        direction -= 1
        if direction < 0:
            direction = 3

def endcheck(x,y):
    if (0 <= x < n) and  (0 <= y < n):
        return True
    else:
        return False

#기타 변수 세팅
# 북 동 남 서
dx =[-1,0,1,0]
dy =[0,1,0,-1]
cnt = 0
direction = 1
x, y = 0, 0
#뱀의 좌표들
snake_loc = deque([[x,y]])

#시뮬레이션 시작
while True:
    cnt += 1
    nx = x + dx[direction]
    ny = y + dy[direction]
    #다음 움직임 위해 방향변환 있는지 체크
    if cnt in movement_change.keys():
        direction_change(movement_change[cnt])
    #종료조건 체크하고 진입
    if endcheck(nx, ny):
        #몸이랑 충돌
        if [nx, ny] in snake_loc:
            break
        if map_data[nx][ny] == 1:
            map_data[nx][ny] = 0
            snake_loc.append([nx, ny])
        elif map_data[nx][ny] == 0:
            snake_loc.append([nx, ny])
            snake_loc.popleft()
    else:
        break
    x, y = nx, ny
print(cnt)






