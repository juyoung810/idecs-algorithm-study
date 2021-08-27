'''
< 왕실의 나이트 >
체스판 8 X 8 좌표평면. 이동시 L자 형태로만 이동. 정원 밖으로는 못나감
수평으로 두 칸 이동 후 수직 한칸 이동 / 수직 두 칸 이동 후 수평 한 칸 이동만 가능
나이트의 위치가 주어졌을 때 나이트가 이동할 수 있는 경우의 수를 출력하는 프로그램
'''

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


# 책 소스코드
'''
나이트는 2가지 경로로 움직일 수 있다. 1) 수평 두 칸 이동 후 수직 한 칸 이동, 2) 수직 두 칸 이동 후 수평 한 칸 이동
나이트의 현재 위치가 주어지면 현재 위치에서 이동 경로를 더한 다음, 8x8 좌표 평면에 있는지 확인하면 된다.
'''

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1    # ord()는 문자의 유니코드 값을 돌려주는 함수.

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2,-1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

# 8가지 방향에 대해서 각 위치로 이동이 가능한지 확인
result = 0
for step in steps:
    # 이동하고자 하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    # 해당 위치로 이동이 가능하다면 카운트 증가
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1

print(result)