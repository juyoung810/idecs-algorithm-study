import sys
input = sys.stdin.readline

C, N = map(int, input().split())
cost_cust = []
cost = []
for i in range(N):
    a = list(map(int, input().split()))
    cost_cust.append(a)
    cost.append(a[0])
m_cost = min(cost)
result = [10**6] * (C+100)
result[0], result[1] = 0, m_cost # 주의
cost_cust.sort(key = lambda x: x[0])

for i in range(0, C+100):
    for j in range(N):
        if i < cost_cust[j][1]:
            continue
        else:
            result[i] = min(result[i-cost_cust[j][1]]+cost_cust[j][0], result[i])
print((min(result[C:])))