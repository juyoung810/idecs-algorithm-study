'''
미로만들기
시작방에서 출발하여 길을 찾아서 끝방으로 가는 것이 목적일 때, 흰 방으로 바꾸어야 하는 검은 방의 최소 개수는?
첫 줄에는 한 줄에 들어가는 방의 수 n이 주어지고, 다음 n개의 줄의 각 줄마다 0과 1이 이루어진 길이가 n인 수열이 주어진다.
0은 검은 방, 1은 흰 방을 나타낸다.

한 지점에서 다른 특정 지점까지의 최단 거리? 라기 보다는 검은 색을 바꿔야 하는 최소 개수...
다익스트라는 한 지점에서 다른 지점으로 가는 최소비용을 알려주기 때문에 검은 방을 만날때 비용이 증가한다고 하면 쉽게 구할 수 있다.
다른 복잡한 방법으로는 왼쪽과 위를 비교해서 더 적은 값을 넣는게 있을듯...

맵을 받아서 그걸 어케 할 것인가!! BFS를 활용한다.
'''

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