N = int(input())
dp = []
for _ in range(N):
    dp.append(list(map(int, input().split())))
if N == 1:
    print(dp[0][0])
else:
    dp[1][0] += dp[0][0]
    dp[1][1] += dp[0][0]
    for i in range(2,N):
        M = len(dp[i])
        for j in range(M):
            if j == 0:
                dp[i][j] += dp[i-1][j]
            elif j == M-1:
                dp[i][j] += dp[i-1][M-2]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    print(max(dp[N-1]))