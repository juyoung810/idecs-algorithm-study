# 크루스칼 알고리즘?
# 두 마을로 분할
# 두 개의 최소 신장 트리 만드는 법
# 한 개의 최소 신장 트리 만든 다음 -> 가장 비용이 큰 간선을 지운다 -> 두개의 최소 신장 트리 완성


n,m = map(int,input().split())

# 집합을 나타내기 위해 각각의 부모를 나타내는 리스트
parent = [0] * (n+1)

for i in range(1,n+1):
    parent[i] = i


# 부모를 찾기 위한 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])

    return parent[x]


# 합 집합 위한 함수
def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 간선의 정보 입력 받기
edges = []

for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))

# 최소 비용 위해 비용 적은 순 정렬
edges.sort()
result = 0
last = 0 # 가장 마지막으로 더해진 edge 가 가장 큰 edge

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        result+= cost
        union_parent(parent,a,b)
        last = cost

print(result-last)
