N = int(input())
tree = [[] for i in range(N + 1)]
for _ in range(N - 1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)


def find_parent(tree, start):
    traced.append(start)
    #print(traced)
    for node in tree[start]:
        if node == 1:
            if traced[0] == start:
                return print(node)
            else:
                return print(traced[1])
        else:
            if node not in visited:
                visited.add(node)
                find_parent(tree, node)


for i in range(2,N+1):
    traced = []
    visited = set()
    find_parent(tree, i)



