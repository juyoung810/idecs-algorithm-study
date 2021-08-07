# 선수강 정해져 있다 -> 위상 정렬
import copy
from collections import deque

# 강의 수 입력 받기
n = int(input())

# 선수과목 저장 위한 graph
graph = [[] for _ in range(n+1)]

# 진입 차수 저장 위한 리스트
indegree = [0] * (n+1)

# 걸리는 시간 저장 위해
time = [0] * (n+1)
# 해당 과목 마다 진입 과목 저장
for i in range(1,n+1):
    edges = list(map(int,input().split()))
    for j in range(len(edges) -1):
        if j == 0:
            time[i] = edges[j]
        else:
            graph[edges[j]].append(i)
            indegree[i] += 1




def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 처음 시작할 때 0인것 넣기
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            # 이미 같으면 안들어가게 하기 위해
            # 선수 과목 now의 결과 + i에 걸리는 시간 vs 이미 i에 걸린 시간 비교해서 더 큰 값 넣기
            result[i] = max(result[i],result[now]+time[i])
            indegree[i] -= 1
            # 새롭게 진입 차수 0인 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)



    for i in range(1,n+1):
        print(result[i])

topology_sort()
