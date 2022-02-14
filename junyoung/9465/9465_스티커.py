import sys
input = sys.stdin.readline

T = int(input())
result = []
for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0]*N for _ in range(2)]
    
    for i in range(N):
        if i ==0:
            dp[0][i] = score[0][i]
            dp[1][i] = score[1][i]
        elif i ==1:
            dp[0][i] = dp[1][0] + score[0][i]
            dp[1][i] = dp[0][0] + score[1][i]
        else:
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + score[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + score[1][i]
    result.append(max(max(dp[0]), max(dp[1])))
    
for i in range(T):
    print(result[i])
    
############################################

t = int(input())
for i in range(t):
    s = []
    n = int(input())
    for k in range(2):
        s.append(list(map(int, input().split())))
    for j in range(1, n):
        if j == 1:
            s[0][j] += s[1][j - 1]
            s[1][j] += s[0][j - 1]
        else:
            s[0][j] += max(s[1][j - 1], s[1][j - 2])
            s[1][j] += max(s[0][j - 1], s[0][j - 2])
    print(max(s[0][n - 1], s[1][n - 1]))