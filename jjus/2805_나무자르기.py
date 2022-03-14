'''
1. 가장 긴 나무보다 절단기 높이가 높을 경우 0m 잘림,
최악의 경우 절단기 높이 0 m 해서 전부 잘라야 할수도 있다.
2. 0 ~ 20 전부 탐색 필요 -> 이진 탐색
3. 이진 탐색 위해 나이 높이 정렬
4. 이진 탐색, 조건에 충족할 경우 답 저장, -> 절단기 높이 더 높이기

'''
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

trees = list(map(int, input().split()))


def find_m(m):
    result = 0
    for tree in trees:
        if tree - m > 0:
            result += tree - m


    return result


# 이진탐색 -> 정렬
trees.sort()

start = 0
end = trees[N - 1]
ans = 0
while start <= end:
    mid = (start + end) // 2  # 절단기 높이
    cut = find_m(mid)
    if cut >= M:
        ans = mid
        start = mid + 1

    else:
        end = mid - 1

print(ans)
