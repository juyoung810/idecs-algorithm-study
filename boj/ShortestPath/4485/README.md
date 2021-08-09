# boj 4485 : 녹색 옷 입은 애가 젤다지 by KKS
> 문제 주소: https://www.acmicpc.net/problem/4485
> 
> 난이도: gold 4

## 1.문제설명
- 테스트케이스 마다 동굴의 정보가 주어짐 
- N by N이고 각 칸마다 숫자가 있는데 지나갈때마다 숫자에 해당하는 루피 잃음
- 이때 잃는 최소 금액을 테스트케이스마다 출력
## 2. 문제 접근법 
- 각 숫자를 가중치라고 생각하고, bfs + heapq 이용해서 다익스트라 구현
## 3.문제 해결 아이디어 or 핵심
- heapq에는 튜플형식으로 (좌표에 해당하는 값, x좌표, y좌표를 넣어줌)
```python
q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    loss[0][0] = 0
```
- 새로운 
``` python
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < distance[nx][ny] :
                    loss[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))
```

## 4.특별히 참고할 사항
- 특별히 없음 
- 이런 종류의 문제에서는 bfs + heapq를 이용해 다익스트라의 개념을 가져옴

## 5.코드구현
``` python
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dij():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)

        if x == n - 1 and y == n - 1:
            print(f'Problem {cnt}: {distance[x][y]}')
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < distance[nx][ny] :
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

cnt = 1
while True:
    n = int(input())
    if n == 0:
        break
    graph = [list(map(int, input().split())) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]

    dij()
    cnt += 1
```