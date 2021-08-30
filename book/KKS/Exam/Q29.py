import sys
input = sys.stdin.readline

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()

min_gap = 1
max_gap = homes[-1] - homes[0]
result = 0

while min_gap <= max_gap:
    gap = (max_gap + min_gap) // 2
    installed = homes[0]
    cnt = 1
    for i in range(1, N):
        if homes[i] >= installed + gap:
            installed = homes[i]
            cnt += 1
    if cnt >= C: # 더 설치된 경우 간격 늘려야함(덜 설치하기 위해) -> 그러기위해선 하한 증가
        #일단 C개 이상 설치했으니 정답을 업데이트해줌
        min_gap = gap + 1
        result = gap
    else: # 덜 설치된 경우 간격을 줄여야함 -> 그러기위해선 상한 증가
        max_gap = gap - 1

print(result)





