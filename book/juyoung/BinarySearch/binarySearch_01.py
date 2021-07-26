# 부품 찾기
# 부품 N개 존재 - 각각 고유한 번호 가진다.
# M개 종류 물품 구매 주문 -> 모두 존재흔지 확인 후 견적서 작성
# 모든 부품 있으면 yes 없으면 no

# 단순 존재 여부 물으므로 set() 집합 자료형 사용하면 효과적이다.
# 수의 범위가 적으므로 계수 정렬을 사용하는 것 또한 효과적이다.

import sys

N = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 사용 위해 정렬하기 (오름차순)
n_list.sort()

M = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().rstrip().split()))


# N개 부품 정렬 위해 필요한 시간 복잡도: O(NlogN)
# M개 부품 이진 탐색 위한 시간 복잡도: O(MlogN)
# 총시간 복잡도: ((M+N)logN)


def binarySearch(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] > target:
        return binarySearch(array, target, start, mid - 1)
    else:
        return binarySearch(array, target, mid + 1, end)



for m in m_list:
    if not binarySearch(n_list, m, 0, N - 1):
        sys.stdout.write("no ")
    else:
        sys.stdout.write("yes ")
