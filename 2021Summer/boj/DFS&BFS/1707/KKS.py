from collections import deque

k = int(input())


def bfs_coloring(connection_info, color):
    cnt = 1
    visited = set()
    visited.add(1)
    queue = deque([1])
    color[1] = 1
    while queue:
        v = queue.popleft()
        cnt += 1
        for node in connection_info[v]:
            if node not in visited:
                visited.add(node)
                queue.append(node)
                color[node] = cnt % 2


def bfs_searching(connection_info, color):
    visited = set()
    visited.add(1)
    queue = deque([1])
    while queue:
        v = queue.popleft()
        color_1 = color[v]
        visited.add(v)
        for node in connection_info[v]:
            if node not in visited:
                color_2 = color[node]

                if color_1 == color_2:
                    return print("NO")

                queue.append(node)
    print("YES")


# 정점의 개수(node) : vertex / 간선의 개수(edge) : edge
for i in range(k):
    vertex, edge = map(int, input().split())
    connection_info = [[] for i in range(vertex + 1)]
    for _ in range(edge):
        n1, n2 = map(int, input().split())
        connection_info[n1].append(n2)
        connection_info[n2].append(n1)

    color = [-1] * (vertex + 1)
    bfs_coloring(connection_info, color)
    bfs_searching(connection_info, color)
