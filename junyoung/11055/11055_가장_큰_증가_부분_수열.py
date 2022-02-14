import sys
input = sys.stdin.readline

N = int(input())
Ai = list(map(int, input().split()))

ch_li = [[] for _ in range(N)]
ch_sum = [0] * N

for i in range(1, N):
    for j in range(i):
        if Ai[i] > Ai[j]:
            ch_li[i].append(j)
for i in range(N):
    _n = len(ch_li[i])           
    if _n ==0:
        ch_sum[i] = Ai[i]
    else:
        M = 0
        for j in ch_li[i]:
            _x = ch_sum[j]
            M = max(M, _x)    
        ch_sum[i] = M + Ai[i]

print(max(ch_sum))


#########################################
n = int(input())
arr = list(map(int,input().split()))
dp = [0] * n

for i in range(n):
    dp[i] = arr[i]
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+arr[i])

print(max(dp))