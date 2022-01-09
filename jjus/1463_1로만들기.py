"""

다이나믹 프로그래밍 - 최적의 방법이 모든 경우에 반례없이 적용된다 -> 가장 큰 수로 최대한 나누는 것이
제일 클 것 -> 10 - 5 - 4 - 2 - 1 보다 10 - 9 - 3 - 1이 더 적음

==> 모든 경우를 고려한다 ->동적 계획법

644ms
"""

import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)

for i in range(2, N+1):
    dp[i] = dp[i - 1] + 1 # 1를 빼는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1) # 3으로 나누는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1) # 2로 나누는 경우

print(dp[N])




