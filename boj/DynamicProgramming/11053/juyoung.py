# 가장 긴 증가하는 부분 수열

import sys

n = int(sys.stdin.readline())

array = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [0] * n # i 까지의 최대 증가하는 부분 수열

dp[0] = 1
for i in range(1,n):
    j = i-1
    while j >= 0:
        if array[j] < array[i] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1
        j -= 1
    if dp[i] == 0: dp[i] = 1


print(max(dp))