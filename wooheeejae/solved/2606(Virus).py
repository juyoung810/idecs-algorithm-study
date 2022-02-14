#바이러스

 # 기본 변수 설정
com = int(input())
line = int(input())
graph = []
for i in range(com+1):
    graph.append([])
visited = [False] * (com + 1)

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
    # 현재 컴퓨터를 방문 처리
    visited[Num] = True
    # 현재 컴퓨터와 연결된 다른 스팟를 재귀적으로 방문
    for i in graph[Num]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, 1, visited)
print(visited.count(True)-1)