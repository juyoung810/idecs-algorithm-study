# 이분 그래프인지 판별
# 연결 정보가 주어지므로 연결리스트로 그래프 구현

# 테스트 케이스 수를 입력 받는다.
from collections import deque
import sys

T = int(sys.stdin.readline())


def BFS(start):
    visited[start] = 1
    q = deque()
    q.append(start)
    # 인접 노드 찾는다.
    while q:
        be = q.popleft()
        for i in graph[be]:
            if visited[i] == visited[be]:
                return False
            elif visited[i] == 0:
                visited[i] = visited[be] + 1
                q.append(i)
    return True


for _ in range(T):
    # 정점 수 , 간선 수를 입력받는다.
    N,E = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(E):
        n1,n2 = map(int,sys.stdin.readline().split())
        # 각각의 node의 index에 해당하는 list에 연결 정보를 더한다.
        graph[n1].append(n2)
        graph[n2].append(n1)
    #print(graph)
    # 방문 정보를 표시한다.
    visited = [0 for _ in range(N+1)]
    isCon = True
    for i in range(1, N+1):
        if visited[i] == 0:
            if not BFS(i):
                sys.stdout.write("NO"+'\n')
                isCon = False
                break
    if isCon:
        sys.stdout.write("YES"+'\n')