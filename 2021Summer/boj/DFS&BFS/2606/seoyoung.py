### 바이러스
## 웜바이러스는 네트워크를 통해 전파. 네트워크 상에서 연결되어 있는 모든 컴퓨터가 바이러스에 걸린다.
## 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터 수를 구하라!
## 컴퓨터의 수 주어지고, 각 컴퓨터에 직접 연결되어 있는 쌍의 수가 주어진다.

from collections import deque

n = int(input())
k = int(input())

# 입력받은 컴퓨터마다의 연결 정보를 저장하기 위한 행렬을 만든다.
network = [[] for i in range(n+1)]

for i in range(k):
    main, connect = map(int, input().split())
    network[main].append(connect)
    network[connect].append(main)

# print(network)

# 감염된 컴퓨터를 확인하기 위해 초기화된 배열 생성
visited = [False for i in range(n + 1)]

def bfs(graph, start, visited):
    # 큐 생성
    queue = deque([start])
    # 첫번째 컴퓨터 감염 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑기
        v = queue.popleft()
        # print(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                 # print(queue)
                visited[i] = True

bfs(network, 1, visited)
print(visited.count(True)-1)