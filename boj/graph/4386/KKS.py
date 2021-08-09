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