T = int(input())
for _ in range(T):
    dp = []
    N, M = map(int, input().split())
    vals = list(map(int, input().split()))
    idx = 0
    for i in range(N):
        dp.append(vals[idx:idx+M])
        idx += M

    for i in range(1,M): #열
        for j in range(N): #행
            if j == 0:
                dp[j][i] += max(dp[j][i-1], dp[j+1][i-1])
            elif j == N-1:
                dp[j][i] += max(dp[j][i-1], dp[j-1][i-1])
            else:
                dp[j][i] += max(dp[j-1][i-1], dp[j][i-1], dp[j+1][i-1])
    result = 0
    for i in range(N):
        result = max(result, dp[i][M-1])
    print(result)
