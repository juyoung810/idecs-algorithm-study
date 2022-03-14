import sys
import heapq
input = sys.stdin.readline
INF = float(1e9)

def solve():
    T = int(input())
    def dijkstra(node, N, M, graph):
        distance = [[INF for _ in range(M+1)] for __ in range(N+1)]
        q = []
        money = 0
        distance[node][money] = 0
        heapq.heappush(q, (distance[node][money], node, money))
        while q:
            cost, pos, money = heapq.heappop(q)
            if distance[pos][money] < cost:
                continue
            for p, c, m in graph[pos]:
                if money + m > M:
                    continue
                c+=cost
                if distance[p][money+m] > c:
                    distance[p][money+m] = c
                    heapq.heappush(q, (c, p, money+m))
        return distance


    for i in range(T):
        N, M, K = map(int, input().split())
        graph = [[]for _ in range(N+1)]
        for j in range(K):
            u,v,c,d = map(int, input().split())
            graph[u].append((v, c, d))
        result = min(dijkstra(1, N, M, graph)[N])

        if result == INF:
            print("Poor KCM")
        else:
            print(result)

solve()