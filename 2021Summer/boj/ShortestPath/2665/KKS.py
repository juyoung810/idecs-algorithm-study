import sys
import heapq

input = sys.stdin.readline
n = int(input())
maze = []
for _ in range(n):
    maze.append(list(map(int, input().rstrip())))
visit = [[0] * n for _ in range(n)]
def dij():
    #하 상 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heapq.heappush(heap, [0, 0, 0])
    visit[0][0] = 1
    while heap:
        a, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if maze[nx][ny] == 0:
                    heapq.heappush(heap, (a+1, nx, ny))
                else:
                    heapq.heappush(heap, (a, nx, ny))

dij()