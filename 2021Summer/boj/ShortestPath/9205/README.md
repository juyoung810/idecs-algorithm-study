# boj 9205 : 맥주 마시면서 걸어가기 by juyoung
> 문제 주소: https://www.acmicpc.net/problem/9205
>
> silver 1

## 문제 해결 방향
- x,y 좌표의 각각의 차의 절댓값을 더해서, 그 차이가 1000 이하이면, 이동할 수 있다. -> 맥주 신경쓰지 않아도 된다.
- 따라서 먼저 그래프의 간선을 조건에 만족하게 만든다.
- 해당 그래프에 플로이드-와샬 알고리즘을 적용해, 연결되어 있는지 확인한다.
- graph[0][n+1] 이 INF 이면, 연결되어 있지 않으므로 sad 아닐 경우, 연결되어 있으므로 happy
- __반복되는 경우 함수로 빼면 시간이 단축된다.__
```python
# 플루이드- 워샬 알고리즘 이용
# 거리 1000 이하인 노드 전부 연결


import sys

input = sys.stdin.readline
INF = int(1e9)
# test 개수 입력 받기
t = int(input())

def find_edge(distance,graph):
    # 전체를 돌면서, 거리 1000 이하이면 간선 연결
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                graph[i][j] = 0
            elif (abs((distance[j][0] - distance[i][0])) + abs((distance[j][1] - distance[i][1]))) <= 1000:
                graph[i][j] = 1


def path(graph):
    # 플루이드 워샬 알고리즘 수행하며, 처음과 페스티벌 연결되었는지 확인
    for k in range(n + 2):
        for a in range(n + 2):
            for b in range(n + 2):
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for _ in range(t):
    # 편의점의 개수 입력받기
    n = int(input())

    distance = []
    for i in range(0, n + 2):
        x, y = map(int, input().split())
        distance.append((x, y))

    graph = [[INF] * (n + 2) for _ in range(n + 2)]

    find_edge(distance,graph)
    path(graph)


    if graph[0][n + 1] != INF:
        print("happy")
    else:
        print("sad")

```