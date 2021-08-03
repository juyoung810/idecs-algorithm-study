# dp 를 모두 0으로 초기화한다.

# 1. n -> n-1 1칸 점프 -> n-3 (반드시)
# 2. n -> n-2 2칸 점프

import sys
n = int(sys.stdin.readline())

stairs = []
# 이차원 행렬로 표현
# O: 점수
# 1: 연속 횟수 count
dp = [0] * n
for _ in range(n):
    stairs.append(int(sys.stdin.readline()))


# 처음 초기화
dp[0] = stairs[0]
if n > 1:
    dp[1] = stairs[0] + stairs[1]
if n > 2:
    # 3번째 칸은
    # 1. 0->2
    # 2. 1-> 2
    dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
if n > 3:
    for i in range(3,n):
        # 1. 마지막 계단의 전 계단을 밟은 경우 n = 4 0->2->4
        # 2. 마지막 계단의 전 계단을 밟지 않은 경우
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3],stairs[i] + dp[i-2])

print(dp[n-1])
