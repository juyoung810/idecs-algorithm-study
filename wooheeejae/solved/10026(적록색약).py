import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
from copy import deepcopy

N = int(input())
answer1 = 0
answer2 = 0
colorGrid = []
tempList = []
for i in range(N):
    temp1 = input()
    for j in temp1:
        tempList.append(j)
    colorGrid.append(tempList)
    tempList = []

graph = deepcopy(colorGrid)

def dfs(x, y, color):
    move = [0, -1, 0, 1, 0] # 상하좌우 확인용
    for i in range(4):
        xPoint = x + move[i]
        yPoint = y + move[i+1]
        if (0 <= xPoint < N) and (0 <= yPoint < N):
            if graph[yPoint][xPoint] == color:
                graph[yPoint][xPoint] = -1
                dfs(xPoint, yPoint, color)

def dfs2(x, y):
    move = [0, -1, 0, 1, 0] # 상하좌우 확인용
    for i in range(4):
        xPoint = x + move[i]
        yPoint = y + move[i+1]
        if (0 <= xPoint < N) and (0 <= yPoint < N):
            if (graph[yPoint][xPoint] == 'R' or graph[yPoint][xPoint] == 'G'):
                graph[yPoint][xPoint] = -1
                dfs2(xPoint, yPoint)

for x in range(N):
    for y in range(N):
        if graph[y][x] == 'R':
            dfs(x, y, 'R')
            answer1 += 1
        elif graph[y][x] == 'G':
            dfs(x, y, 'G')
            answer1 += 1
        elif graph[y][x] == 'B':
            dfs(x, y, 'B')
            answer1 += 1

graph = deepcopy(colorGrid)

for x in range(N):
    for y in range(N):
        if graph[y][x] == 'R':
            dfs2(x, y)
            answer2 += 1
        elif graph[y][x] == 'G':
            dfs2(x, y)
            answer2 += 1
        elif graph[y][x] == 'B':
            dfs(x, y, 'B')
            answer2 += 1


print(f'{answer1} {answer2}')