N = int(input())

dp = [0] * N
dp[0]  = 1

x2 = x3 = x5 = 0
next2, next3, next5 = 2, 3, 5

for i in range(1,N):
    dp[i] = min(next2, next3, next5)
    if dp[i] == next2:
        x2 += 1
        next2 = dp[x2] * 2
    if dp[i] == next3:
        x3 += 1
        next3 = dp[x3] * 3
    if dp[i] == next5:
        x5 += 1
        next5 = dp[x5] * 5

print(dp[N-1])