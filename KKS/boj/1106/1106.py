import sys
input = sys.stdin.readline
INF = 1e9
C, N = map(int, input().split()) #c ->늘려야할 최소고객수, N - > 도시개수
advertise = []

for _ in range(N):
    temp = list(map(int, input().split())) #비용, 고객수
    advertise.append(temp)

advertise.sort(key=lambda x : x[0])

dp = [INF]*(C+100)
dp[0] = 0

for cost, new_pep in advertise:
    for i in range(new_pep, C+100):
        dp[i] = min(dp[i-new_pep] + cost, dp[i])

print(min(dp[C:]))