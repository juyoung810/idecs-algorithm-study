import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(start):
    visited.add(start)
    next_node = path[start]
    if next_node not in visited:
        dfs(next_node)

tc = int(input())
for _ in range(tc):
    visited = set()
    ans = 0
    n = int(input())
    path =[0] + list(map(int, input().split()))
    visited.add(0)

    for i in range(1, n+1):
        if i not in visited:
            dfs(i)
            ans += 1
    print(ans)