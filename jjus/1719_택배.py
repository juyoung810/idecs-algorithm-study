import sys
import heapq

input = sys.stdin.readline

N, M = map(int, input().split())
# (n+1) X (n+1) 그래프 생성 : undirected weighted graeph
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    graph[n1].append([n2, w])
    graph[n2].append([n1, w])

result = [[0 for _ in range(N + 1)] for _ in range(N + 1)]


def my_print():
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if result[i][j] == -1:
                print("-", end=" ")
            else:
                print(result[i][j], end=" ")
        print()


def dijkstra(start):
    fringe = []  # fringe set (총 weight, node번호, start node 번호)
    # start-start 처리
    result[start][start] = -1
    # start 노드와 인접한 노드들 fringe에 추가
    for n_n, n_w in graph[start]:
        heapq.heappush(fringe, [n_w, n_n, n_n])
    # fringe set 비워질 때 까지
    while fringe:
        new_w, new_n, new_s = heapq.heappop(fringe)
        result[start][new_n] = new_s  # 결과 값 append
        print(graph[new_n])
        for node in graph[new_n]:
            # 아직 결과가 정해지지 않은 경우
            if result[start][node[0]] == 0:
                # 이미 fringe set에 존재하는 경우
                if fringe and node[0] in list(zip(*fringe))[1]:
                    # 값 update가 더 작은 경우
                    al_index = list(zip(*fringe))[1].index(node[0])
                    if node[1] + new_w < fringe[al_index][0]:
                        fringe[al_index][0] = node[1] + new_w
                        fringe[al_index][2] = new_s  # 시작 번호 update
                else:
                    heapq.heappush(fringe, [new_w + node[1], node[0], new_s])
            else:
                print(node)


for i in range(1, N + 1):
    dijkstra(i)  # 각 node 별로 dijkstra

my_print()
