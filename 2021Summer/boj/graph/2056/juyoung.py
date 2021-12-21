# 선행 관계가 없는 작업들은 동시에 수행 가능
# 선행 관계 -> 위상 정렬 알고리즘
# 선행 관계가 같은 level에 들어간다면, 시간이 빠른 순으로 정렬되어야 한다.

import sys
from collections import deque

input = sys.stdin.readline

# 작업의 갯수 입력 받기
n = int(input())

# 1 ~ N 까지의 작업 시간 저장
times = [0] * (n + 1)

# 집입 차수 저장 위한 리스트
indegree = [0] * (n + 1)

# 작업들의 선행 관계를 저장,표현하기 위한 그래프
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    times[i] = temp.pop(0)
    indegree[i] += temp.pop(0)
    for before in temp:
        # before 다음 i 번째 일 실행
        graph[before].append(i)

# 시간 저장 위한 dp
dp = [0] * (n+1)
# 위상 정렬

q = deque()
# 진입 차수 0 인 것 q에 먼저 넣기
for i in range(1, n + 1):
    if indegree[i] == 0:
        dp[i] = times[i]
        q.append(i)

while q:

    now = q.popleft()
    # now와 연결된 edge의 진입 차수 다 -1
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + times[i],dp[i])
        if indegree[i] == 0:
            # q에 들어가는 작업이 끝나느 시간은, 선행 작업이 끝난 시간 다음 + 자기 시간
            q.append(i)


# 제일 마지막 작업이 끝나는 시간 = times 테이블에서 가장 큰 수
print(max(dp))