import sys

input = sys.stdin.readline

N = int(input())

t_list = []
p_list = []

for _ in range(N):
    t,p = map(int,input().split())
    t_list.append(t)
    p_list.append(p)


dp = [ 0 for _ in range(N+1)]

for i in range(N-1,-1,-1):
    if i + t_list[i] > N: # 퇴사 날짜 넘은 경우
        dp[i] = dp[i+1] # 전날까지 금액으로담
    else:
        # i일에 상담을 하는 경우 VS 상담하지 않고 전날 금액 그대로
        dp[i] = max(dp[i+t_list[i]]+p_list[i],dp[i+1])

print(dp[0])
