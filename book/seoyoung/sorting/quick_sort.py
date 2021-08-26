'''
< 퀵 정렬(quick sort) >
기준 데이터를 설정한 후 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작
피벗(교환하기 위한 기준)이 사용됨.
피벗보다 큰 수와 작은 수가 엇갈리면, 작은 수와 피벗의 위치를 서로 교환한다.
피벗을 기준으로 왼쪽, 오른쪽 리스트에서 각각 동일한 과정을 반복한다.(재귀)
'''

# 가장 직관적인 형태의 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    pivot = start  # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    while left <= right:   # 인덱스가 범위 안에 있는 동안
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left < end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right:  # 엇갈렸다면(왼쪽에서는 큰 수 찾고, 오른쪽에서는 작은 수 찾는데 왼쪽이 더 작다면):
            array[right], array[pivot] = array[pivot], array[right]  # 작은 데이터와 피벗을 교체
        else:  # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체. 피벗을 기준으로 왼쪽에는 작은 데이터, 오른쪽에는 큰 데이터 오도록
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)



# 파이썬의 장점을 살린 퀵 정렬 소스코드

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort_easy(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]  # 피벗은 첫 번째 원소
    tail = array[1:]  # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]  # 분할된 왼쪽 부분. 첫 번째 원소보다 작은 모든 원소
    right_side = [x for x in tail if x > pivot]  # 분할된 오른쪽 부뷴. 첫 번째 원소보다 큰 모든 원소

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 후, 전체 리스트 반환
    return quick_sort_easy(left_side) + [pivot] + quick_sort_easy(right_side)

print(quick_sort_easy(array))


## 퀵 정렬의 평균 시간 복잡도는 O(NlogN), 최악의 경우 시간 복잡도가 O(N^2) : 데이터가 이미 정렬되어 있는 경우
