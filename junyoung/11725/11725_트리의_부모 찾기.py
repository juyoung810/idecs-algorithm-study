from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 반복 제한 풀기(default : 1000)

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [-1] * (N+1)
for _i in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def dfs(start):
    for i in graph[start]:
        if parent[i] == -1:
            parent[i] = start
            dfs(i)
dfs(1)
for i in range(2, N+1):
    print(parent[i])


from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
parent = [-1] * (N+1)
for i in range(N-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        _node = q.popleft()
        for i in graph[_node]:
            if parent[i] == -1:
                parent[i] = _node
                q.append(i)
    return parent

bfs(1)
for i in range(2, N+1):
    print(parent[i])

############################################
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
tree = [[] for _ in range(n+1)]
par = [-1]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    for i in tree[n]:
        if par[i] == -1:
            par[i] = n
            dfs(i)
            
dfs(1)
for i in range(2,n+1):
    print(par[i])
    

###################################    
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    while q:
        node = q.popleft()
        for i in graph[node]:
            if parent[i] == 0:
                parent[i] = node
                q.append(i)

    return parent
bfs()
for i in parent[2:]:
    print(i)