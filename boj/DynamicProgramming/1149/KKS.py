#집의 갯수 입력
n = int(input())
cache = [0]*n
cost = []
for i in range(n):
    # R G B
    cost.append(list(map(int,input().split())))

#초기조건
for i in range(1, n):
    cost[i][0] = cost[i][0] + min(cost[i-1][1], cost[i-1][2])
    cost[i][1] = cost[i][1] + min(cost[i - 1][0], cost[i - 1][2])
    cost[i][2] = cost[i][2] + min(cost[i - 1][0], cost[i - 1][1])

print(min(cost[n-1][0],cost[n-1][1],cost[n-1][2]))