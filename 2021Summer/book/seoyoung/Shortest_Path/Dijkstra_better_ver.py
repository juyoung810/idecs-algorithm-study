# 방법 2. 개선된 다익스트라 알고리즘
'''
최악의 경우에도 시간 복잡도 O(ElogV)를 보장 : V는 노드의 개수, E는 간선의 개수
힙 자료구조를 사용. 힙은 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 우선순위 큐를 구현하기 위해 사용하는 자료구조
파이썬에서는 우선순위 큐가 필요할 때 PriorityQueue 혹은 heapq를 사용. heapq가 더 빠르게 동작
우선순위 큐 라이브러리에 데이터의 묶음을 넣으면, 첫 번째 원소를 기준으로 우선순위 설정
최소힙 : 값이 낮은 데이터가 먼저 삭제, 최대 힙 : 값이 큰 데이터가 먼저 삭제
파이썬의 우선순위 큐 라이브러리는 최소 힙 구조를 기반. 다익스트라 최단 경로 알고리즘에서 비용이 적은 노드를 우선하여 방문하므로 그대로 사용
최소 힙을 최대 힙처럼 사용하기 위해서는 일부러 우선순위에 해당하는 값에 음수 부호를 붙여서 넣었다가, 나중에 우선순위 큐에서 꺼낸 다음에 다시 원래의 값으로 돌리는 방법 사용
우선순위 큐는 힙 자료구조 뿐만 아니라, 리스트를 이용해서 구현할 수 있다. 근데 힙으로 구현하는게 훨씬 빠름

최소 힙을 다익스트라 최단 경로 알고리즘에 적용하자!
단순히 우선순위 큐를 이용해서 시작 노드로부터 '거리'가 짧은 노드 순서대로 큐에서 나올 수 있도록 다익스트라 알고리즘 작성
최단 거리를 저장하기 위한 1차원 리스트는 아까와 같이 그대로 이용, 현재 가장 가까운 노드를 저장하기 위한 목적으로만 우선순위 큐를 추가로 이용
'''

# 개선된 다익스트라 알고리즘 소스코드 (get_smallest_node() 함수를 작성할 필요가 없다!)

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)   # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])