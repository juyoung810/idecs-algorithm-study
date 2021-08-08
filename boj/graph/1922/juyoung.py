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
