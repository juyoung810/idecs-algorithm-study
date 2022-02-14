'''
< 호텔 >
- 홍보를 할 수 있는 도시, 각 도시별 홍보 비용, 늘어나는 고객 수 정보
- 고객을 적어도 C명 늘이기 위해 형택이가 투자해야 하는 돈의 최솟값은?

< 아이디어 >
-
'''

import sys
input = sys.stdin.readline
INF = 1e9

c, n = map(int, input().split())
d = [INF] * (c+100)
d[0] = 0

info = [list(map(int, input().split())) for _ in range(n)]
info = sorted(info, key=lambda x: x[0])

for cost, cust in info:
    for i in range(cust, c+100):
        d[i] = min(d[i-cust] + cost, d[i])

print(min(d[c:]))