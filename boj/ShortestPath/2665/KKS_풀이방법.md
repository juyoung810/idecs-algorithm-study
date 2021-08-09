# boj 2665 : 미로만들기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/2665
> 
> 난이도: gold 4

## 1.문제설명
- n by n 사이즈 바둑판에 모양으로 총 n^2 개의 방이 있음 시작점(0,0) 에서 끝(n-1, n-1)까지 가려한다
- 하지만 검은방은 못지나가서 흰방으로 어쩔수없이 바꿔야함. 
- 가장 적게 바꾸며 갈때 몇번 바꿔야할까?
## 2. 문제 접근법 
- 방의 색을 바꾼다를 어떻게 구현할것인가...
- 일단 이렇게 미로 형식으로 된 문제에서는 bfs + heapq를 이용해야할듯
## 3.문제 해결 아이디어 or 핵심
- 최단경로로 이동/  이동한곳이 검은방일때는 a에 += 1 로 힙에 넣어줌 
- a를 하나의 가중치라고 생각하면될듯
- ```python
            if 0<= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if maze[nx][ny] == 0:
                    heapq.heappush(heap, (a+1, nx, ny))
                else:
                    heapq.heappush(heap, (a, nx, ny))


## 4.특별히 참고할 사항
없음

## 5.코드구현
``` python
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
```