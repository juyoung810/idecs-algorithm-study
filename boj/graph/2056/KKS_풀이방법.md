# boj 2056 : 작업 by KKS
> 문제 주소: https://www.acmicpc.net/problem/2056
> 
> 난이도: gold 4

## 1.문제설명
- 수행해야 할 작업들 N개가 있음
- K번 작업을 시작하기 전에 반드시 먼저 완료되어야하는 작업들의 번호는 모두 1이상 K-1이하
- 모든 작업을 완료하기 위해 필요한 최소시간을 구하면됨
- 단 서로 선행관계가 없는 작업들은 동시에 수행 가능
## 2. 문제 접근법
- 생각이 안나서 인터넷에 검색을 해봄
- k번 작업에 대해 선행관계에 있는 작업들의 번호가 모두 1이상 K-1이하이기 때문에 dp로 해결가능
- 해당 작업에 걸리는 시간을 times에 저장, 선행작업을 graph에 저장
- for문을 돌면서 해당작업에 필요한 선행 작업들의 max시간을 더한다
- 작업에 필요한 시간들 중 최댓값 출력
## 3.문제 해결 아이디어 or 핵심
- 선행관계가 없는 작업들이 동시에 수행가능한 점이 기존의 위상정렬과 차이

## 4.특별히 참고할 사항


## 5.코드구현
``` python
import sys
input = sys.stdin.readline
n = int(input())
times = [0] * (n+1) #해당작업에 걸리는 시간
graph = {} #key: n번째 작업, value = n번째 작업을 위한 선행작업
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    times[i] = lst[0]
    if lst[1] == 0: # 선행작업들이 없으면
        continue # 패스
    for j in lst[2:]: #선행작업들이 있으면
        if i in graph: #i번째 작업에 j를 추가해줌
            graph[i].append(j)
        else: #없으면 [j]를 추가해줌
            graph[i] = [j]

for i in range(1, n+1):
    if i in graph:
        time = 0
        for j in graph[i]:
            time = max(time, times[j])
        times[i] += time

print(max(times))
```