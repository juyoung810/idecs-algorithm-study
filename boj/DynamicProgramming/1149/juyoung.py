# dp = N * 3 행렬로 만든다.
# 입력 받은 rgb는 일차원 행렬로 그때 그때 받는다.

import sys

n = int(sys.stdin.readline())
# n*3 행렬 만들어 1001로 초기화한다.
dp = []


for i in range(n):
    rgb = list(map(int,sys.stdin.readline().split()))
    # 초기화 해주기
    if i == 0:
        dp.append(rgb[0])
        dp.append(rgb[1])
        dp.append(rgb[2])

    # 각각의 값 비교해서 update
    else:
        r = dp[0]
        g = dp[1]
        b = dp[2]

        dp[0] = 1000 * n + 1
        dp[1] = 1000 * n + 1
        dp[2] = 1000 * n + 1

        # r
        if dp[1] > r + rgb[1]: dp[1] = r + rgb[1]
        if dp[2] > r + rgb[2]: dp[2] = r + rgb[2]
        # g
        if dp[0] > g + rgb[0]: dp[0] = g + rgb[0]
        if dp[2] > g + rgb[2]: dp[2] = g + rgb[2]
        # b
        if dp[0] > b + rgb[0]: dp[0] = b + rgb[0]
        if dp[1] > b + rgb[1]: dp[1] = b + rgb[1]

sys.stdout.write(str(min(dp)))