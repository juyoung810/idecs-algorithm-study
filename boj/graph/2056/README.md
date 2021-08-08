# boj 2056 : 작업 by juyoung
> 문제 주소: https://www.acmicpc.net/problem/2056
>
> gold 4

# 문제 해결 방향
- 선행 관계가 존재하므로 위상 정렬 알고리즘
- 선행 관계가 없는 작업들은 동시에 작업 수행이 가능하다. 
  따라서, dp 테이블을 통해 선행 작업이 하나 끝날 때 마다, __해당 작업이 끝나는 시간 + 내 작업 끝나는 시간 VS 원래 dp에 저장된 끝나는 시간__
  을 비교해서 더 큰 것이 해당 작업이 끝나는 시간으로 설정된다.
  
### 주의할 점
- 100 0,10 0, 5 2 1 2 -> 이렇게 주어질 경우 10이 끝난 다음에 5를 시작한다고 착각하기 쉽다. 
100이 끝나야 작업을 수행할 수 있는 것 이므로, __선행 작업이 끝날 때 마다 == 진입차수가 하나 -1 될 때 마다__ 시간을 계산해서 저장해야 한다.
  
### 소스 코드
1. 작업 개수를 입력받아 graph, 진입 차수 저장 리스트, 시간 저장 리스트 생성
```python
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
```
2. n개의 작업에 대한 시간, 선행 작업의 수, 선행 작업을 입력 받기
- 선행 작업의 수가 미리 주어지므로, 한번만 update 하면 된다.
```python
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    times[i] = temp.pop(0)
    indegree[i] += temp.pop(0)
    for before in temp:
        # before 다음 i 번째 일 실행
        graph[before].append(i)
```
3. 끝나는 시간 저장 위해 dp를 생성, 선입선출 위해 deque 생성
```python
# 시간 저장 위한 dp
dp = [0] * (n+1)
# 위상 정렬
q = deque()
```
4. 진입 차수 0 인 것 먼저 q에 넣기
- 진입 차수가 0이면 끝나는 시간은 자기 자신의 작업 시간이다.
```python
# 진입 차수 0 인 것 q에 먼저 넣기
for i in range(1, n + 1):
    if indegree[i] == 0:
        dp[i] = times[i]
        q.append(i)
```

5. q가 빌 때 까지 반복하며, 위상 정렬 실행
- 진입차수가 - 1 될 때 마다, 해당 작업의 끝나는 시간을 `끝난 작업의 시간 + 내 작업 시간 vS 원래 내 작업이 끝나는 시간` 비교해 더 큰 값으로 
  끝나는 시간 update
  
```python
while q:

    now = q.popleft()
    # now와 연결된 edge의 진입 차수 다 -1
    for i in graph[now]:
        indegree[i] -= 1
        dp[i] = max(dp[now] + times[i],dp[i])
        if indegree[i] == 0:
            # q에 들어가는 작업이 끝나느 시간은, 선행 작업이 끝난 시간 다음 + 자기 시간
            q.append(i)

```
6. 출력: dp 테이블에서 가장 큰 값 = 모든 작업이 끝난 시간
- 항상 n 번 작업이 마지막으로 끝나는 것이 아님을 유의해야한다.
```python
# 제일 마지막 작업이 끝나는 시간 = times 테이블에서 가장 큰 수
print(max(dp))
```