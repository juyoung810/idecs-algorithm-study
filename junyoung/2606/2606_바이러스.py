from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
n = int(input())
graph = [[] for _ in range(N+1)] # 편의상 0 추가
for _i in range(n):
    _x, _y = map(int, input().split())
    graph[_x].append(_y)
    graph[_y].append(_x)
bfs_check= [0] * (N+1)
bfs_route = []

def bfs(start):
    q= deque()
    q.append(start)
    bfs_check[start] = 1
    while q:
        a = q.popleft()
        bfs_route.append(a)
        for i in graph[a]:
            if bfs_check[i] ==0:
                bfs_check[i]=1
                q.append(i)
    return bfs_route
bfs(1)
print(len(bfs_route)-1)


###################################

import sys
input = sys.stdin.readline

N = int(input())
n = int(input())
linked = []
result = []
for i in range(n):
    link = list(map(int, input().split()))
    linked.append(link)

def find_set(linked, num):
    check = []
    for i, j in linked:
        if i == num :
            check.append(j)
        elif j == num:
            check.append(i)
    while check:
        a = check.pop()
        if a not in result:
            result.append(a)
            find_set(linked, a)
            
    return result
x = len(find_set(linked, 1)) -1
print(x)