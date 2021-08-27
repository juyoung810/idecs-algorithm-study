'''
커리큘럼
듣고자 하는 N개의 강의 정보가 주어졌을 때, N개의 강의에 대하여 수강하기까지 걸리는 최소 시간을 각각 출력하라.
위상 정렬 알고리즘의 응용문제.
인접한 노드에 대해 현재보다 강의 시간이 더 긴 경우를 찾는다면, 더 오랜 시간이 걸리는 경우의 시간 값을 저장하는 방식으로 결과 테이블 갱신
리스트의 경우, 단순히 대입 연산을 하면 값이 변경될 때 문제가 발생할 수 있기 때문에, 리스트의 값을 복제해야 할 때는 deepcopy() 함수 사용

각 강의 수강하기까지의 최소 시간을 result 리스트 변수에 담기
처음에 각 강의 시간은 time 리스트 변수에 담겨 있는데, deepcopy() 함수를 이용하여 time 리스트 변수의 값을 복사하여 result 리스트 변수의 값
으로 설정하는 작업 수행
'''

from collections import deque
import copy

# 노드의 개수 입력받기
v = int(input())
# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]
# 각 강의 시간을 0으로 초기화
time = [0] * (v+1)

# 방향 그래프의 모든 간선 정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]   # 첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)  # x를 들은 후 들어야 하는 수업들을 저장하기

# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time)    # 알고릐즘 수행 결과를 담을 리스트
    q = deque()     # 큐 기능을 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now = q.popleft()
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()