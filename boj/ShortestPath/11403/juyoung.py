# 가중치 없는 방향 그래프 G
# 모든 정점(i,j) 에 대해 i->j 경로 유무 판별

import sys
INF = int(1e9)
input = sys.stdin.readline

n = int(input())

#최단 경로 담는 graph
graph = []
# 인접행렬 입력 받기
for i in range(n):
    graph.append(list(map(int,input().split())))



# 플루이드 워샬
for k in range(n):
    for a in range(n):
        for b in range(n):
            # 경로가 존재하지 않는다면
            if graph[a][b] != 1:
                # 둘 중 하나라도 0 이 아니면 0 이상이 될 것
                graph[a][b] = min(graph[a][k],graph[k][b])




# 출력
for a in range(n):
    for b in range(n):
        # if graph[a][b] == -1:
        #     print(0,end = " ")
        # else:
        #     print(1,end = " ")
        if graph[a][b]:
            print(1,end = " ")
        else:
            print(0,end = " ")
    print()

