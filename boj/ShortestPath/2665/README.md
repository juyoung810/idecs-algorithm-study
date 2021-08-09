# boj 2665 : 미로만들기 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/2665
>
> gold 4

## 문제
시작방에서 출발하여 끝방까지 가는 것이 목적일 때, 흰 방으로 바꾸어야 하는 검은 방의 최소 개수를 구하라.

## 문제 해결 방향
한 지점에서 다른 특정 지점까지의 최소 비용을 구하는 문제이기 때문에 다익스트라 알고리즘을 이용하면 된다.\
검은 방을 만날 때 비용을 증가시키면 쉽게 구할 수 있다.

지도형태의 2차원 배열로 지도를 받아, BFS때 사용했던 좌표이동을 이용한다.

다르게 복잡한 방법을 생각했던 것은 현 위치의 왼쪽과 위쪽의 값 중 더 작은 값을 대상으로, 현 위치의 값이 0이면 1을 더하고 1이면 그대로 넣어주는 방법을 생각했다.

## 소스코드
입력 데이터를 저장해준다. 방 수열 정보는 문자열 리스트로 받아 저장한다. \
방문기록을 저장할 리스트도 방문하지 않음으로 초기화한다.
```python
import sys
import heapq

input = sys.stdin.readline

# 입력 데이터 받기
n = int(input())    # 한 줄에 들어가는 방의 수

rooms = []  # 방 수열. 1은 흰 방, 0은 검은 방
for i in range(n):
    rooms.append(list(input()))

# 이동할 네 방향 설정
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

# 방문 기록 저장할 리스트
visited = [[False] * n for i in range(n)]
```
최소비용을 구해야 하기 때문에 최소힙을 이용한 다익스트라 함수를 구현한다.\
시작노드를 받아 방문처리를 해주고, 힙에 집어넣는다. 계속 비용이 제일 작은 방향으로 움직이고, 큐에 집어넣는다.
```python
# 다익스트라 함수 : 시작노드 비용을 0으로 설정해서 힙에 집어넣기. 계속 움직이면서 비용과 좌표 뽑기.
def dijkstra(sx, sy):
    q = []
    heapq.heappush(q, (0, sx, sy))  # 시작 좌표와 비용 초기화 해주기
    visited[sx][sy] = True  # 방문처리

    # 큐에 값이 들어있는 동안
    while q:
        # 가장 비용이 작은 노드에 대한 정보 꺼내기
        cnt, now_x, now_y = heapq.heappop(q)

        # 목표지점에 도달시 cnt 반환
        if now_x == n-1 and now_y == n-1:
            return cnt

        # 이동하기
        for i in range(4):
            x = now_x + dx[i]
            y = now_y + dy[i]

            # 범위를 벗어나는 경우 실행 안함
            if x < 0 or x >= n or y < 0 or y >= n:
                continue

            # 이미 방문한 방은 넘어감
            if visited[x][y]:
                continue

            # 방문했다고 표시해주기
            visited[x][y] = True

            # 흰 방을 만나면 그냥 진행
            # 검은 방을 만나면 값을 1로 바꿔주고 cnt에 1을 더해준다
            if rooms[x][y] == '1':
                heapq.heappush(q, (cnt, x, y))
            else:
                rooms[x][y] = '1'
                heapq.heappush(q, (cnt + 1, x, y))


print(dijkstra(0, 0))
```