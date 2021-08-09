N, D = map(int, input().split())
short_cut = [list(map(int, input().split())) for _ in range(N)]
distance = [i for i in range(D+1)]
for i in range(D+1):
    if i > 0:
        distance[i] = min(distance[i], distance[i-1]+1)
    for s, e, d in short_cut:
        if i == s and e <= D and distance[i]+d < distance[e]:
            distance[e] = distance[i]+d
print(distance[D])