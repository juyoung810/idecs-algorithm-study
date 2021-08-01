n, k = map(int, input().split())
value = []
weight = []
for i in range(n):
    w, v = map(int, input().split())
    value.append(v)
    weight.append(w)
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for w in range(k+1):
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif weight[i-1] <= w:
            dp[i][w] = max(value[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])
        else:
            dp[i][w] = dp[i-1][w]
print(dp[n][k])