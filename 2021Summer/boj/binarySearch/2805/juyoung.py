# 나무 M 미터 필요
# 절단기 높이 H -> H이상 다 절단 -> 잘린 것 집에 들고 간다.
# 절단기 높이 0~
# 필요한 만큼만 집으로 가져간다. 적어도  미터의 나무 집에 가져가기 위해 절단기에 설정할 수 있는 높이의 최댓값


# 절단기의 높이 H : 0 ~ max(주어진 나무의 길이)

import sys
n,m = map(int,sys.stdin.readline().rstrip().split())
trees = list(map(int,sys.stdin.readline().rstrip().split()))

# 이진 탐색 통해 절단기의 길이의 범위를 줄여나간다.


start = 0
end = max(trees)
# 절단기의 길이
result = 0

def cutting_result(mid,trees): ## 함수를 이용하면 시간을 아낄 수 있다.
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    return total


while start <= end:
    # 잘린 나무의 길이 저장값

    mid = (start + end) //2

    # 잘린 나무의 길이가 부족한 경우 절단기의 길이를 줄여서 더 많이 절단할 수 있도록 한다. (왼쪽 부분 탐색)
    if cutting_result(mid,trees) < m:
        end = mid -1
    # 잘린 길이가 충분한 경우 더 최적의 절단기 길이를 찾기 위해 절단기 길이 늘린다.(오른쪽 부분 탐색)
    else:
        result = mid # 일단 조건 만족했으므로 해당 절단기 길이를 저장한다
        start = mid +1

sys.stdout.write(str(result))