# boj 11403 : 경로찾기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/11403
> 
> 난이도: silver1

## 1.문제설명
- 첫째줄에 정점의 개수 N이 주어지고 [1,100] 
- 둘째줄부터 그래프의 인접행렬이 주어짐
- 총 N개의 줄에 걸쳐서 문제의 정답을 인접행렬로 출력
- 정점 i에서 j로 갈수있으면 i번째 줄의 j번 숫자를 1로, 없으면 0으로
## 2. 문제 접근법 
- N이 100개 이하니깐 플로이드 와샬 알고리즘 사용할수 있음
## 3.문제 해결 아이디어 or 핵심
- 플로이드 와샬에서는 비용을 최소비용으로 업데이트 해줬음 하지만 이번에는
- 갈수 있는지 없는지 여부를 업데이트

## 4.특별히 참고할 사항
- 3중 for문을 이용할 예정
- 첫번째 for문은 거쳐서 가는 노드를, 두번째 for문은 시작, 마지막 for문은 도착 노드임

## 5.코드구현
``` python
import sys
input = sys.stdin.readline
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1

for row in graph:
    for col in row:
        print(col, end = " ")
    print()
```