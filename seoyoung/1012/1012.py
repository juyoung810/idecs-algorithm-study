'''
< 유기농 배추 >
0은 배추가 심어져 있지 않은 땅, 1은 배추가 시머져 있는 땅.
이어져 있는 배추는 배추지렁이의 보호를 받을 수 있을 때, 배추지렁이는 몇마리가 필요할까?

< 아이디어 >
1. 맵을 받아서 배추 위치를 표시한다.
2. 배추가 있을 때(1을 만날 때) bfs를 실행해 주변 배추를 확인하고 0으로 바꾼뒤 배추지렁이 수를 추가한다.
'''

import sys
input = sys.stdin.readline

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue.pop()
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if 0 <= q < n and 0 <= w < m and graph[q][w] == 1:
                graph[q][w] = 0
                queue.append([q, w])

for case in range(T):
    n, m, k = map(int, input().split())
    graph = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        graph[a][b] = 1
    for q in range(n):
        for w in range(m):
            if graph[q][w] == 1:
                bfs(q, w)
                graph[q][w] = 0
                cnt += 1
    print(cnt)