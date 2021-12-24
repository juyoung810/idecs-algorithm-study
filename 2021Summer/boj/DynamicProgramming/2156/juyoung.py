# 연속 세잔 불가

# 1. 해당 칸 전 칸 밟은 경우
# 2. 해당 칸 전 칸 밟지 않은 경우

import sys

n = int(sys.stdin.readline())

dp = [0] * n

wines = []
for _ in range(n):
    wines.append(int(sys.stdin.readline()))

dp[0] = wines[0]
if n > 1:
    # 2개 있으면 두개 더한게 최대
    dp[1] = wines[0] + wines[1]

if n > 2:
    # 자기거 안 더한게 더 클수도!
    # 3개 있으면 0->1 or 0->2 or 1->2 가 최대
    dp[2] = max(dp[1],wines[0] + wines[2],wines[1]+wines[2])
if n > 3:
    # 4개 이상
    for i in range(3,n):
        # 해당 칸 이전 칸 밟은 경우
        # 해당 칸 이전 칸 밟지 않은 경우
        # 이전 dp 까지가 더 큰 경우
        # 4 : 0->1->3->4, 0->2->->4 or 이전 값
        dp[i] = max(dp[i-1],dp[i-3]+wines[i-1]+wines[i],dp[i-2]+wines[i])


print(dp[n-1])