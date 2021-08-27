# boj 4386 : 별자리 만들기 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/4386
>
> gold 4

## 문제
n개의 별들을 이어서 별자리를 만들 때, 모든 별들은 별자리 위의 선을 통해 직/간접적으로 이어져 있어야 한다.\
별들이 2차원 평면 위에 놓여 있고, 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 들 때, 별자리를 만드는 최소 비용을 구하라!

## 문제 해결 방향
크루스칼 알고리즘을 이용해 푼다.\
간선에 대한 정보가 없으므로, 별들 사이의 거리를 계산해서 간선에 대한 정보를 저장해 준다.

## 소스코드
별의 좌표를 받아 몇 번째 별인지와 함께 좌표 정보를 기록한다.\
거리, 부모노드, 결과값을 저장할 변수를 만든다.
```python
import math

# 별의 개수
n = int(input())

# 별의 좌표 받기
stars = []
for i in range(n):
    x, y = map(float, input().split())
    stars.append((i, x, y))  # 몇 번째 별인지와 좌표 정보 기록

distance = []
parent = [0] * (n+1)
result = 0
```
각각의 별들에 대해, 좌표 사이의 거리와 시작별, 끝별의 간선 정보를 기록해준다.\
간선 정보를 거리 순으로 정렬한다.
```python
for start in stars:
    for end in stars:
        dx = start[1] - end[1]
        dy = start[2] - end[2]
        d = math.sqrt(dx*dx + dy*dy)
        distance.append((d, start[0], end[0]))  # 거리, 시작노드, 도착노드 저장하기

# 간선을 비용순으로 정렬
distance.sort()
```
크루스칼 알고리즘을 통해 최소 비용 신장 트리를 찾는다.
```python
# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

# 간선을 하나씩 확인하며
for edge in distance:
    dist, s, e = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, s) != find_parent(parent, e):
        union_parent(parent, s, e)
        result += dist

print(result)
```
