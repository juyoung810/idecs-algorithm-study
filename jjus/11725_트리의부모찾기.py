"""
bfs 통해 자신을 queue에 집어 넣은 것이 부모

568ms -> 함수로 고치면 더 빨라질듯
"""
import sys
input = sys.stdin.readline

N = int(input())
tree = [[] for i in range(N+1)]

for _ in range(N-1):
    a,b = map(int, input().split(" "))
    tree[a].append(b)
    tree[b].append(a)

#bfs 실행
parent = [0] * (N+1)
visited = [0] * (N+1)

q = list()
q.append(1)
while q:
    p = q.pop(0)
    for s in tree[p]:
        if visited[s] == 0:
            visited[s] = 1
            parent[s] = p
            q.append(s)

for i in range(2,N+1):
    print(parent[i])


