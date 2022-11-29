#DFS와 BFS

# 큐(Queue) 구현을 위해 deque 라이브러리 사용
from collections import deque

 # 기본 변수 설정
spot, line, startNum = map(int, input().split())
graph = []
for i in range(spot + 1):
        graph.append([])
visited = [False] * (spot+1)

 # 문제 풀이
 # 인접 리스트 만들기

for i in range(line):
    n, m = list(map(int, input().split()))
    graph[n].append(m)
    graph[n].sort()
    graph[m].append(n)
    graph[m].sort()

 # DFS함수 정의
def dfs(graph, Num, visited):
    # 현재 스팟를 방문 처리
    visited[Num] = True
    print(Num, end=' ')
    # 현재 스팟과 연결된 다른 스팟를 재귀적으로 방문
    for i in graph[Num]:
        if not visited[i]:
            dfs(graph, i, visited)

 # BFS함수 정의
def bfs(graph, Num, visited):
    queue = deque([Num])
    # 현재 노드를 방문 처리
    visited[Num] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        n = queue.popleft()
        print(n, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph, startNum, visited)
print()
visited = [False] * (spot+1)
bfs(graph, startNum, visited)

#
# from collections import deque
#
# # BFS 함수 정의
# def bfs(graph, start, visited):
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드를 방문 처리
#     visited[start] = True
#     # 큐가 빌 때까지 반복
#     while queue:
#         # 큐에서 하나의 원소를 뽑아 출력
#         v = queue.popleft()
#         print(v, end=' ')
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
#         for i in graph[v]:
#             if not visited[i]:
#                 queue.append(i)
#                 visited[i] = True
#
#  # DFS 함수 정의
# def dfs(graph, v, visited):
#     # 현재 노드를 방문 처리
#     visited[v] = True
#     print(v, end=' ')
#     # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(graph, i, visited)
#
# # 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# graph = [
#   [],
#   [2, 3, 8],
#   [1, 7],
#   [1, 4, 5],
#   [3, 5],
#   [3, 4],
#   [7],
#   [2, 6, 8],
#   [1, 7]
# ]
#
# # 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
# visited = [False] * 9
#
# # 정의된 DFS 함수 호출
# dfs(graph, 1, visited)