from collections import deque
import sys
input = sys.stdin.readline
k = int(input())


def bfs(start):
    color[start] = 1
    queue = deque()
    queue.append(start)
    while queue:
        v = queue.popleft()
        for node in graph[v]:
            if color[node] == 0:
                color[node] = -color[v]
                queue.append(node)
            else:
                if color[node] == color[v]:
                    return False
    return True


for i in range(k):
    vertex, edge = map(int, input().split())
    isTrue = True
    graph = [[] for i in range(vertex+1)]
    color = [0 for i in range(vertex+1)]
    for j in range(edge):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    for y in range(1, vertex+1):
        if color[y] == 0:
            if not bfs(y):
                isTrue = False
                break
    print("YES" if isTrue else "No")