'''
< 점프 >
- NXN 게임판에 수가 적혀져 있다. 가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프
- 각 칸에 적힌 수는 현재 칸에서 갈 수 있는 거리. 오른쪽 or 아래로만 이동 가능
- 0은 진행 막는 종착점
- 규칙에 맞게 이동할 수 있는 경로의 개수 구하라

< 아이디어 >
- 각각의 칸에 대해서 이동할 수 있는 범위의 칸을 갱신한다.
'''


# 이렇게 했을 때 왜 틀리는지 잘 모르겠음
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0:
            print(d[i][j])
            break
        k = board[i][j]
        if j+k < n:
            d[i][j+k] += d[i][j]
        if i+k < n:
            d[i+k][j] += d[i][j]


import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = [[0]*n for _ in range(n)]
d[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            print(d[i][j])
            break
        k = board[i][j]
        if j+k < n:
            d[i][j+k] += d[i][j]
        if i+k < n:
            d[i+k][j] += d[i][j]