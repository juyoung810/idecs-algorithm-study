# 랜선의 길이 0 ~ 최대 길이
n, m = map(int, input().split())

lans = []
for _ in range(n):
    lans.append(int(input()))

# 이진 탐색 통해 찾는다.
def cutting_result(key):
    total = 0
    for lan in lans:
        if lan >= key:
            total += lan // key

    return total

# 랜선의 최소 길이가 1임을 유의한다.
start = 1
end = max(lans)
result = 0
while start <= end:
    mid = (start + end) // 2
    # 컷팅 갯수가 충분하지 않은 경우 단위를 줄인다.

    if cutting_result(mid) < m:
        end = mid - 1
    # 컷팅 길이가 충분한 경우, 단위를 늘려 더 크게 만들 수 있도록 한다
    else:
        result = mid
        start = mid + 1

print(result)
