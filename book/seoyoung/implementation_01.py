### 왕실의 나이트
## 체스판 8 X 8 좌표평면. 이동시 L자 형태로만 이동. 정원 밖으로는 못나감
## 수평으로 두 칸 이동 후 수직 한칸 이동 / 수직 두 칸 이동 후 수평 한 칸 이동만 가능
## 나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램

loc = input()
col = 'abcdefgh'
ways = [[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2],[2,-1],[2,1]]
cnt = 0

# 열 좌표 찾기
col = col.find(loc[0]) + 1
start = [col, int(loc[1])]

for way in ways:
    result = [start[0] + way[0], start[1] + way[1]]
    if 0 < result[0] < 9 and 0 < result[1] < 9:
        cnt += 1

print(cnt)