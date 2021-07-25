# DFS(Depth-First Search). 깊이 우선 탐색. 깊은 부분을 우선적으로 탐색

## 그래프의 표현
# 인접 행렬 방식
INF = 999999999  # 무한의 비용 선언

graph = [   # 2차원 리스트를 이용해 인접 행렬 표현
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)


# 인접 리스트 방식 : 연결리스트를 이용해서 구현. 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결해 저장
graph = [[] for _ in range(3)]  # 행(row)이 3개인 2차원 리스트로 인접 리스트 표현

graph[0].append((1, 7))  # 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((2, 5))

graph[1].append((0, 7))  # 노드 1에 연결된 노드 정보 저장(노드, 거리)

graph[2].append((0, 5))  # 노드 2에 연결된 노드 정보 저장(노드, 거리)

print(graph)


## 인접 행렬 방식은 모든 관계를 저장하므로 노드 개수가 많을수록 메모리가 불필요하게 낭비
## 인접 리스트 방식은 연결된 정보만을 저장하기 때문에 메모리를 효율적으로 사용, 그러나 정보를 얻는 속도가 느림