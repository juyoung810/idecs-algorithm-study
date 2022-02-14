import sys
input = sys.stdin.readline

N= int(input())

days = []
values = []
for _ in range(N):
    d,m = map(int,input().split())
    days.append(d)
    values.append(m)

dp = [0] * (N+1) # 시작하는 날 금액 끝난 날에 들어간다.
M = 0 # 누적 금액
for i in range(N):
    M = max(M,dp[i]) # i 시점에 최대 금액
    if i + days[i] <=  N:  # N일 내로 일이 끝난다면
        dp[i+days[i]] = max(M+values[i],dp[i+days[i]]) # 기존에 i 일 끝났을 때 까지 번 돈 VS i시점에 일 새로 시작했을 때 벌 돈


print(dp)
print(max(dp))