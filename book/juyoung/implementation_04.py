import datetime

start_time = datetime.datetime.now()
# 북:0, 서 : 3, 남 :2, 동:1
#  북 동 남 서
# (북쪽으로 떨어진 칸의 수 , 서쪽으로 떨어진 칸의 수)
# (x,y)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# N : 행, M: 열
N, M = map(int, input().split())

x, y, direction = map(int, input().split())

# 전체 map의 정보 받기
map_index = []
for i in range(N):
    map_index.append(list(map(int, input().split())))

# 전체 map의 visit 정보 ( 전체 0 초기화)
visited = [[0] * M for _ in range(N)]

# 가장 먼저 주어진 위치 방문
visited[x][y] = 1
count = 1
# 회전한 수 count ( 회전한 수가 4이면 모두 회전한 것)
turn_count = 0
# (direction -1 +4 ) % 4 => 서쪽 회전
while True:
    # 왼쪽 회전
    direction = (direction - 1 + 4) % 4
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전 후 바라 보는 방향이 육지이면서, 방문하지 않은 칸일 경우 이동
    if map_index[nx][ny] == 0 and visited[nx][ny] == 0:
        visited[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_count = 0
    # 회전 후 바라 보는 방향이 바다이거나 , 이미 방문한 칸일 경우
    else:
        turn_count+=1

    # 모든 방향을 다 갈 수 없는 경우
    if turn_count == 4:
        # 방향 뒤 돌기 -> 원래 방향에서 - 하면 반대로 뒤돈다.
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤 돈 경우 육지일 경우:
        if map_index[nx][ny] == 0:
            x, y = nx, ny
            turn_count = 0
        else: break


print(count)

end_time = datetime.datetime.now()
elapsed_time = end_time - start_time
# ms
ms_elapsed_time = elapsed_time.microseconds / 1000
print(str(ms_elapsed_time))
