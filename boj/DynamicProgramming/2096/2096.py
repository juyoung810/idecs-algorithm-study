n = int(input())
min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]


for i in range(n):
    _temp = list(map(int, input().split()))

    max_dp[1][0] = _temp[0] + max(max_dp[0][0], max_dp[0][1])
    max_dp[1][1] = _temp[1] + max(max_dp[0][0], max_dp[0][1], max_dp[0][2])
    max_dp[1][2] = _temp[2] + max(max_dp[0][1], max_dp[0][2])

    min_dp[1][0] = _temp[0] + min(min_dp[0][0], min_dp[0][1])
    min_dp[1][1] = _temp[1] + min(min_dp[0][0], min_dp[0][1], min_dp[0][2])
    min_dp[1][2] = _temp[2] + min(min_dp[0][1], min_dp[0][2])

    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]

print(max(max_dp[1]), min(min_dp[1]))