from collections import deque
from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

n = int(input())
graph = []
for i in range(n):
    _temp = list(input())
    graph.append(_temp)
cw_graph = deepcopy(graph)
normal_cnt = 0
cw_cnt = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs_normal(graph, x, y, prev):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == prev:
            if graph[nx][ny] == 'R':
                graph[nx][ny] = '0'
                dfs_normal(graph, nx, ny, 'R')
            elif graph[nx][ny] == 'G':
                graph[nx][ny] = '1'
                dfs_normal(graph, nx, ny, 'G')
            elif graph[nx][ny] == 'B':
                graph[nx][ny] = '2'
                dfs_normal(graph, nx, ny, 'B')

def dfs_cw(graph, x, y, prev):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if prev == 'B':
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == prev:
                if graph[nx][ny] == 'R':
                    graph[nx][ny] = '0'
                    dfs_cw(cw_graph, nx, ny, 'R')
                elif graph[nx][ny] == 'G':
                    graph[nx][ny] = '1'
                    dfs_cw(cw_graph, nx, ny, 'G')
                elif graph[nx][ny] == 'B':
                    graph[nx][ny] = '2'
                    dfs_cw(cw_graph, nx, ny, 'B')
        else:
            if 0 <= nx < n and 0 <= ny < n and (graph[nx][ny] == 'R' or graph[nx][ny] == 'G'):
                if graph[nx][ny] == 'R':
                    graph[nx][ny] = '0'
                    dfs_cw(cw_graph, nx, ny, 'R')
                elif graph[nx][ny] == 'G':
                    graph[nx][ny] = '1'
                    dfs_cw(cw_graph, nx, ny, 'G')
                elif graph[nx][ny] == 'B':
                    graph[nx][ny] = '2'
                    dfs_cw(cw_graph, nx, ny, 'B')

for x in range(n):
    for y in range(n):
        if graph[x][y].isalpha():
            if graph[x][y] == 'R':
                normal_cnt += 1
                graph[x][y] = '0'
                dfs_normal(graph, x, y, 'R')
            elif graph[x][y] == 'G':
                normal_cnt += 1
                graph[x][y] = '1'
                dfs_normal(graph, x, y, 'G')
            elif graph[x][y] == 'B':
                normal_cnt += 1
                graph[x][y] = '2'
                dfs_normal(graph, x, y, 'B')

for x in range(n):
    for y in range(n):
        if cw_graph[x][y].isalpha():
            if cw_graph[x][y] == 'R':
                cw_cnt += 1
                cw_graph[x][y] = '0'
                dfs_cw(cw_graph, x, y, 'R')
            elif cw_graph[x][y] == 'G':
                cw_cnt += 1
                cw_graph[x][y] = '1'
                dfs_cw(cw_graph, x, y, 'G')
            elif cw_graph[x][y] == 'B':
                cw_cnt += 1
                cw_graph[x][y] = '2'
                dfs_cw(cw_graph, x, y, 'B')

print(normal_cnt, cw_cnt)
