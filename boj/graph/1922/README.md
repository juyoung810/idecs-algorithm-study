# boj 1922 : 네트워크 연결 by juyoung
> 문제 주소: https://www.acmicpc.net/problem/1922
>
> gold 4


# 문제 해결 방향
- 컴퓨터를 모두 연결하고, 최소 비용이 되어야한다.
- 그래프를 최소 비용을 연결하기 위해 사이클이 존재하지 않아야 한다. -> 신장 트리
- 최소 신장 트리 -> __크루스칼 알고리즘 이용__

# 소스 코드
```python
# 전체 연결을 판별 -> 크루스칼 알고리즘

import sys

input = sys.stdin.readline


# 부모 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:  # 부모가 자기 자신이 아닌 경우
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# union 함수
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 컴퓨터 수
n = int(input())
# 연결할 수 있는 선의 수 - union 연산의 수
m = int(input())

# 부모를 저장하기 위한 리스트
parent = [0] * (n + 1)

# 자기 자신을 부모로 초기화
for i in range(1, n + 1):
    parent[i] = i

edges = []
for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))  # cost순으로 정렬 위해

edges.sort()  # edge 적은 순으로 정렬

total = 0

for edge in edges:
    cost, a, b = edge
    if find_parent(parent,a) != find_parent(parent,b):  # 이미 연결되어 있지 않다며
        total += cost
        union_parent(parent, a, b)


print(total)

```

# 시간 복잡도
- O(ElogE)
- 간선을 정렬해야 하기 때문
- 서로소 집합 알고리즘보다 정렬이 더 오래 걸리기 때문에, 서로소 집합 알고리즘의 시간 복잡도는 신경쓰지 않아도 된다.