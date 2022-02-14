 # 기본 변수 설정
N = int(input())
Map = [list(map(int, input().split())) for i in range(N)] # 지도
answer = [[0 for i in range(N)] for i in range(N)] # 어느 좌표에 갈 수 있는 경우의 수
answer[0][0] = 1

 # 문제 풀이
def moveCheck(x, y):
    # 아래로 이동 가능할 경우
    if Map[y][x] + y < N:
        # answer[y][x]에 갈 수 있는 방법을 전 칸과 더함
        answer[Map[y][x] + y][x] += answer[y][x]
    # 오른쪽으로 이동 가능할 경우
    if Map[y][x] + x < N:
        # answer[y][x]에 갈 수 있는 방법을 전 칸과 더함
        answer[y][Map[y][x] + x] += answer[y][x]

# Map[y][x] = 점프거리
# answer[y][x] = 이 좌표로 갈 수 있는 경우의 수
for y in range(N):
    for x in range(N):
        # 점프거리가 0이 아니고
        # answer에서 0,0을 제외하고 그 곳에 갈 수있는 방법이 있어야함
        if Map[y][x] != 0 and answer[y][x] != 0:
            moveCheck(x, y)

print(answer[-1][-1])