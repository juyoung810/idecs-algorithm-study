import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dij():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    loss[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {loss[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < loss[nx][ny] :
                    loss[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    loss = [[INF] * n for _ in range(n)]

    dij()
    cnt += 1