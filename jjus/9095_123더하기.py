'''
dp로 모든 경우를 따져서 푼다

점화식
A(n) = A(n-1) + A(n-2) + A(n-3)

n = 4
3 + 1 : 3를 만드는 경우에 전부 1를 추가한다
2 + 2 : 2를 만드는 경우에 전부 2를 추가한다
1 + 3 : 1를 만드는 경우에 전부 3를 추가한다.
'''
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * 12

dp[1] = 1
dp[2] = 2
dp[3] = 4

count = 1
for i in range(4,11+1):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(N):
    n = int(input())
    print(dp[n])

