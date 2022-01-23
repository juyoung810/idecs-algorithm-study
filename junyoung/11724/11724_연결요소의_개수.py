import sys
input = sys.stdin.readline # 안하면 시간초과 발생
sys.setrecursionlimit(10**6) # 런타임 에러 방지 - 재귀

N, M = map(int,input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    _x, _y = map(int, input().split())
    graph[_x].append(_y)
    graph[_y].append(_x)

dfs_check = [0] * (N+1)
def dfs(start):
    dfs_check[start] = 1
    for i in graph[start]:
        if dfs_check[i] ==0:
            dfs(i)

adj_count = 0
for i in range(1, N+1):
    if dfs_check[i] == 0:
        dfs(i)
        adj_count +=1
        
print(adj_count)