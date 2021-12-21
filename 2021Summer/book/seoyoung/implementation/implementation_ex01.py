### 상하좌우
## N X N 크기의 정사각형 공간. (1, 1) 에서 출발
## 계획서의 L R U D 명령에 따라서 이동. 최종 도착 지점의 좌표 출력
## 공간 밖은 무시한다.

n = int(input())
plan = input().split()
x, y = 1, 1

for way in plan:
    if way == 'L' and y != 1:
        y -= 1
    elif way == 'R' and y != n:
        y += 1
    elif way == 'U' and x != 1:
        x -= 1
    elif way == 'D' and x != n:
        x += 1

print(x, y)


## 책 예시 답안

n = int(input())
x, y = 1, 1
plans = input().split()

# 계획서에 따른 이동 방향.
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 좌표로 찍으면 더 편하겠구나! 여러 조건 안달아도 돼서

# 이동 계획 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)


