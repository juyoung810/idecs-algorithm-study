# 미래도시
# 1->k->n 최단 경로 구하기
# 전형적인 플루이드 워샬 알고리즘
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 대각선 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a ==b:
            graph[a][b] = 0

# 간선 정보 입력 받기
for _ in range(m):
    i,j = map(int,input().split())
    graph[i][j] = 1
    graph[j][i] = 1


for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k] + graph[k][b])

x,k = map(int,input().split())
if graph[x][k] != INF and graph[k][x] != INF:
    print(graph[1][k]+graph[k][x])
else: print(-1)