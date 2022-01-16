import sys
N = int(input())
sys.setrecursionlimit(10**9)
tree = [[] for i in range(N + 1)]
parent = [0 for _ in range(N+1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

def DFS(start, tree, parent):
    for i in tree[start]:
        if parent[i] == 0:
            parent[i] = start
            DFS(i, tree, parent)

DFS(1, tree, parent)

for i in range(2, N+1):
    print(parent[i])