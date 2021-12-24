n, m = map(int, input().split()) #가로, 세로
x, y, direction = map(int, input().split())
map_visited = [[0] * m for _ in range(n)]
map_visited[x][y] = 1
map_info = [list(map(int, input().split())) for _ in range(n)]
#북0 동1 남2 서3
#좌표(r,c) 각각 북, 서에서 떨어진 칸의 갯수
dx =[-1,0,1,0]
dy =[0,1,0,-1]
cnt = 1
turn_time = 0

def turn_left():
    global direction
    direction -= 1
    if direction < 0:
        direction = 3

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if map_info[nx][ny] == 0 and map_visited[nx][ny] == 0:
        map_visited[nx][ny] = 1
        x, y = nx, ny
        cnt += 1
        turn_time =0
        continue
    else:
        turn_time +=1
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if map_info[nx][ny] == 0:
            x,y = nx, ny
        else:
            break
        turn_time = 0
print(cnt)