'''
< KCM Travle >
- 최대 M원까지의 비용 부담. M원 이하로 사용하면서 도착할 수 있는 가장 빠른 길을 선택하자.
- 공항들간 티켓가격과 이동시간이 주어질 때, 인천에서 LA로 갈 수 있는 가장 빠른 길을 찾아라!

< 아이디어 >
- 각 공항에 대해서, 해당 공항에 가는데 걸리는 시간과 비용을 저장한다.
- M원 이하로 사용할 때, 가장 빨리 가는 길을 저장한다.
- 소요시간이 짧지만 비싼 경우, 소요시간이 길지만 비용이 싼 경우를 모두 탐색해야 한다!

< 알아둘 점 >
INF 를 sys.maxsize로 표현 가능
'''

import sys
input = sys.stdin.readline
INF = sys.maxsize

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    info = [[] for _ in range(N+1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        info[u].append([v,c,d])

    dp = [[INF for _ in range(M+1)] for _ in range(N+1)]
    dp[1][0] = 0

    # dp의 모든 도시에 대해서, 모든 비용을 확인한다.
    for c in range(M+1):
        for d in range(1, N+1):
            if dp[d][c] == INF :
                continue
            t = dp[d][c]
            for dv,dc,dd in info[d]:
                if dc+c > M:
                    continue
                dp[dv][dc+c] = min(dp[dv][dc+c], t+dd)

    result = min(dp[N])

    if result == INF:
        print('Poor KCM')
    else:
        print(result)