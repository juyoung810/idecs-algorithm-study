import sys
INF = float(1e9)
def solve():
    n, m, k = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(k):
        n1, n2, cost, flight_time = map(int, sys.stdin.readline().rstrip().split())
        graph[n1].append((n2, cost, flight_time))
    distance = [[INF] * (m + 1) for _ in range(n + 1)]
    distance[1][0] = 0
    for money in range(m + 1):
        for node in range(1, n + 1):
            if distance[node][money] != INF:
                for n2, cost, flight_time in graph[node]:
                    if money + cost <= m:
                        distance[n2][money + cost] = min(distance[n2][money + cost], distance[node][money] + flight_time)
    rst = min(distance[n])
    if rst == INF:
        print("Poor KCM")
    else:
        print(rst)


t = int(input())
for _ in range(t):
    solve()