from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _i in range(N+1)] # 편의를 위해 1개 더 추가
for i in range(M):
    x, y= map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
for i in range(len(graph)):
    graph[i].sort()
dfs_check = [0] *(N+1)
dfs_route = []
bfs_check = [0] *(N+1)
bfs_route = []

def dfs(start):
    dfs_check[start] = 1
    dfs_route.append(start)
    for i in graph[start]:
        if dfs_check[i] == 0:
            dfs(i)
    return dfs_route
for i in dfs(V):
    print(i, end= ' ')
  
    
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        a = q.popleft()
        if bfs_check[a] == 0:
            bfs_check[a] =1
            bfs_route.append(a)
            q.extend(graph[a])
    return bfs_route
print()
s = ''
for i in bfs(V):
    s += (str(i)+ ' ')
print(s)
        
#####################################
# 처음 짠 코드
import sys
input = sys.stdin.readline

N, M, V = list(map(int, input().split()))
linked=[]
for i in range(M):
    linked.append(list(map(int, input().split())))

def link_node(linked, start):
    next = []
    for i in range(M):
        if linked[i][0] == start: 
            next.append(linked[i][1])
        elif linked[i][1] == start:
            next.append(linked[i][0])
    next.sort()
    return next

def graph(linked):
    graph = []
    for i in range(1, N+1):
        _link = link_node(linked, i)
        graph.append(_link)
    return graph

dfs_route = [V]
gp = graph(linked)
node_check = [False for i in range(N)]

def dfs(start):
    node_check[start-1] = True
    for node in gp[start-1]:
        if node_check[node-1] == False:
            dfs_route.append(node)
            dfs(node)
            # node_check[node-1] = True : 함수 앞에서 해주기 때문에 불필요한 코드
    return dfs_route
for i in dfs(V):
    print(i, end=' ')

check = [False for i in range(N)]
def bfs(start):    
    check[start-1] = True
    left = [start]
    route = []
    while left:
        _a = left.pop(0)
        route.append(_a)
        for _i in gp[_a-1]:
            if check[_i-1] ==False:
                left.append(_i)
                check[_i-1] = True
    return route

print('')
for i in bfs(V):
    print(i, end=' ')

    
#################################################
# 따온 코드

from collections import deque
import sys
read = sys.stdin.readline

def bfs(v):
  q = deque()
  q.append(v)       
  visit_list[v] = 1   
  while q:
    v = q.popleft()
    print(v, end = " ")
    for i in range(1, n + 1):
      if visit_list[i] == 0 and graph[v][i] == 1:
        q.append(i)
        visit_list[i] = 1

def dfs(v):
  visit_list2[v] = 1        
  print(v, end = " ")
  for i in range(1, n + 1):
    if visit_list2[i] == 0 and graph[v][i] == 1:
      dfs(i)

n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)] 
visit_list = [0] * (n + 1)
visit_list2 = [0] * (n + 1)

for _ in range(m):
  a, b = map(int, read().split())
  graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)