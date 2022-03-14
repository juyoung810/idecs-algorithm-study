n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]
shortest_node = [[0] * (n+1) for _ in range(n+1)]
for x in range(1, n+1):
    for y in range(1, n+1):
        if x == y:
            graph[x][y] = 0
            shortest_node[x][y] = '-'


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)
    graph[b][a] = min(graph[b][a], c)
    shortest_node[a][b] = b
    shortest_node[b][a] = a


for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if graph[a][k] + graph[k][b] < graph[a][b]:
                graph[a][b] = graph[a][k] + graph[k][b]
                shortest_node[a][b] = shortest_node[a][k]

shortest_node = shortest_node[1:]

shortest_node = map(lambda x : x[1:], shortest_node)

for item in shortest_node:
    print(*item)
