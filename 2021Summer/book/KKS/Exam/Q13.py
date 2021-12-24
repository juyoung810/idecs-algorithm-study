from itertools import combinations
N, M = map(int, input().split())
street = []
chicken = []
house = []
distance = []
for i in range(N):
    street.append(list(map(int, input().split())))
for i in range(N):
    for j in range(N):
        if street[i][j] == 1:
            house.append((i,j))
        elif street[i][j] == 2:
            chicken.append((i,j))

comb = combinations(chicken, M)
result = int(1e9)
for c in comb:
    total_distance = 0
    for home in house:
        min_d = min([abs(home[0] - store[0]) + abs(home[1] - store[1]) for store in c])
        total_distance += min_d
    if total_distance < result:
        result = total_distance

print(result)