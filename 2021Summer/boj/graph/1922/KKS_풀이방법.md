# boj 1922 : 네트워크 연결 by KKS
> 문제 주소: https://www.acmicpc.net/problem/1922
> 
> 난이도: gold 4

## 1.문제설명
- 크루스칼 알고리즘을 이용하는 문제
## 2. 문제 접근법 
- 책에 나온 그대로 구현하면 된다.
## 3.문제 해결 아이디어 or 핵심

## 4.특별히 참고할 사항
- 알면 풀고 모르면 못푼다 이해하고, 빠르게 구현할수 있게 필요한 부분은 암기가 필요할듯..

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


edges =[]
result = 0
n = int(input())
m = int(input())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

for _ in range(m):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
```