import sys
input = sys.stdin.readline

N = int(input())
board = []
for i in range(N):
    _temp = list(map(int, input().split()))
    board.append(_temp)

dp = [[0]*N for i in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        else:
            down = i + board[i][j]
            right = j + board[i][j]

            if down < N:
                dp[down][j] += dp[i][j]
            if right < N:
                dp[i][right] += dp[i][j]
print(dp[N-1][N-1])
