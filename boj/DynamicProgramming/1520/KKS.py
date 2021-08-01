import sys
sys.setrecursionlimit(10**8)
#n:세로, m:가로
n, m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

dp = [[-1] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x,y):
    if x == 0 and y == 0:
        return 1
    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and  0 <= ny < m:
                if graph[x][y] < graph[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]

print(dfs(n-1,m-1))