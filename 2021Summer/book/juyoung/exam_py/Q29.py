# 공유기 설치
# 집 N개가 수직선 위에 위치
# 집에 공유기 C개 설치
# 한 집에 공유기 하나 설치, 가장 인접한 두 공유기 사이 거리 가능한 크게
# C개의 공유기 N개의 집에 적당히 설치해서, 가장 이넙한 두 공유기 사이의 거리 최대
# 가장 인접한 두 공유기 사이의 최대 거리 출력

import sys

input = sys.stdin.readline

# n,c 입력 받기
n, c = map(int, input().split())

# 집 좌표 입력 받기 -> 이분 탐색 위해 오름 차순 정렬
homes = []
for _ in range(n):
    homes.append(int(input()))

homes.sort()

start = 1  # 최소 단위거리 = 1 (겹치는 집 좌표 없으므로)
end = max(homes) - min(homes)  # 최대 단위 거리
while start <= end:
    mid = (start + end) // 2
    # mid가 단위 거리일 때, 배치할 수 있는 공유기 수 구하기
    count = 1
    install = homes[0]  # 첫번째는 무조건 설치해야 거리가 최대
    for i in range(1, n):
        if homes[i] >= install + mid:  # 단위 거리 충족했으면
            count += 1
            install = homes[i]

    # 와이파이 개수가 C 보다 작으면 더 설치 해야한다. -> 간격을 좁힌다.
    if count < c:
        end = mid - 1
    # 와이파이 개수가 C 보다 크면 덜 설치해야 한다. -> 간격을 넓힌다
    else:
        start = mid + 1
        answer = mid # 간격 넓혀서 더 큰 최대 거리 구할 수 도 있으니까..

print(answer)

