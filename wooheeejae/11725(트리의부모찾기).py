#트리의부모찾기
 # 기본 변수 설정
tree = int(input())
line = tree - 1
graph = []
for i in range(tree + 1):
    graph.append([])

 # 문제풀이
 # 인접 리스트 만들기
for i in range(line):
    n, m = list(map(int, input().split()))
    graph[n].append(m)
    graph[m].append(n)

 # 부모 출력
for j in range(0, line):
    print(graph[j+2][0])