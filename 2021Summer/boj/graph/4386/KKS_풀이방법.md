# boj 4386 : 별자리 만들기 by KKS
> 문제 주소: https://www.acmicpc.net/problem/4386
> 
> 난이도: gold4

## 1.문제설명
- n개의 별을 이으려고함
- 별자리를 만드는 최소비용
## 2. 문제 접근법 
- 이 문제는 노드사이의 가중치가 주어지지 않음
- 따라서 모든 가중치를 직접 구해서 넣어야됨
- 그 후로는 크루스칼 알고리즘과 같음
## 3.문제 해결 아이디어 or 핵심
```python
for i in range(N):
    for j in range(i+1, N):
        a = star[i]
        b = star[j]
        dist = round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 2)
        edges.append((dist, i, j))
edges.sort()
```

## 4.특별히 참고할 사항


## 5.코드구현
``` python
import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
star = []
parent = [0] * (N+1)
edges = []

for i in range(1, N+1):
    parent[i] = i

for i in range(N):
    star.append(list(map(float, input().split())))

for i in range(N):
    for j in range(i+1, N):
        a = star[i]
        b = star[j]
        dist = round(((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5, 2)
        edges.append((dist, i, j))
edges.sort()

ans = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        ans += cost

print(ans)
```