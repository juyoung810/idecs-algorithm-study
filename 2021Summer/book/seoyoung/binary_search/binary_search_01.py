### 부품 찾기
## N개의 부품이 있고, M개 종류의 부품이 있는지 확인해야 한다.
## 손님이 요청한 부품 번호의 순서대로 부품을 확인. 있으면 yes 없으면 no 출력. 구분은 공백

## 먼저 매장 내 N개의 부품을 번호 기준으로 정렬 후 찾고자 하는 부품이 각각 매장에 존재하는지 검사.

## 이진 탐색을 이용한 답안 예시
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# 가게의 부품 개수 입력
n = int(input())
# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()  # 이진 탐색을 수행하기 위해 사전에 정렬 수행
# M(확인 요청한 부품 개수) 입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    result = binary_search(array, i, 0, n-1)
    if result != Nond:
        print('yes', end=' ')
    else:
        print('no', end=' ')



## 계수 정렬을 이용한 예시
n = int(input())
array = [0] * 1000001

# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1

# 확인 요청한 부품 개수 입력받기
m = int(input())
# 확인 요청한 전체 부품 번호를 공백으로 구분해 입력
x = list(map(int, input().split()))

# 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    # 해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end=' ')
    else:
        print('no', end=' ')


## 단순히 특정한 수가 한 번이라고 등장했는지 검사. 집합 자료형 이용해 해결 가능

n = int(input())
# 전체 부품 번호 입력받아서 집합 자료형에 기록
array = set(map(int, input().split()))

m = int(input())
# 확인 요청한 전체 부품 번호 공백으로 구분해 입력
x = list(map(int, input().split()))

# 확인 요청한 부품 번호 하나씩 화인
for i in x:
    # 부품 존재 확인
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')