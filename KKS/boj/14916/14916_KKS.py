n = int(input())
INF = float("inf")
dp = [INF] * (n + 1)
coins = [2, 5]

def get_min_chagne(n):
    if n <= 1:
        return -1
    if n == 2:
        return 1
    if n == 3:
        return -1
    if n == 4:
        return 2

    for coin in coins:
        dp[coin] = 1

    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] = min(dp[i - coin] + dp[coin], dp[i])

    if dp[n] != INF:
        return dp[n]
    else:
        return -1

print(get_min_chagne(n))