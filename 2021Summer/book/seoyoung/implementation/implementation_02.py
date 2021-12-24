'''
< 게임 개발 >
맵의 각 칸은 (A, B), A는 북족으로부터 떨어진 칸의 개수, B는 서쪽으로부터 떨어진 칸의 개수. 좌표!
캐릭터는 상하좌우로 이동 가능. 바다로는 못감
현재 위치에서 현재 방향 기준 왼쪽 방향부터 차례대로 갈 곳 정함
캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸 존재시 왼쪽 방향으로 회전 후 왼쪽으로 한 칸 전진. 가보지 않은 칸 없으면 회전만 수행
네 방향 모두 이미 가본 칸이거나 바다로 되어있으면 방향 유지한 채로 한 칸 뒤로 가고 1단계로 돌아감. 뒤쪽이 바다면 멈춤
이동을 마친 후 캐릭터가 방문한 칸의 수 출력
'''

'''
전형적인 시뮬레이션 문제.
일반적으로 방향을 설정해서 이동하는 문제 유형에서는 dx, dy라는 별도의 리스트를 만들어 방향을 정하는 것이 효과적이다.
-> 반복문을 이용하여 모든 방향을 차례대로 확인 가능. 유용
'''

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 작성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 멥 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction    # 외부에서 선언된 전역변수 사용
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

# 정답 출력
print(count)