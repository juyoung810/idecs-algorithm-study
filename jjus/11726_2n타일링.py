'''
n - 1 : 의 경우에 세워져 있는 한 개의 타일이 붙는다.
n - 2:  의 경우에 누워져 있는 두 개의 타일이 붙는다.
'''
import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
dp[1] = 1
if N > 1: dp[2] = 2


for i in range (3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N] % 10007)
