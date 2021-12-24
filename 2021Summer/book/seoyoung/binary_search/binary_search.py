### 이진 탐색(binary search)
## 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘.
## 시작점, 끝점, 중간점의 세 가지 변수를 사용한다.
## 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는다
# 중간점이 실수일 때는 소수점 이하를 버린다.
## 한 번 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어든다. 시간 복잡도가 O(logN)이다.

# 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search_reculsive(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search_reculsive(array, target, start, mid-1) # 끝점을 중간점의 왼쪽으로 옮긴다
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search_reculsive(array, target, mid+1, end)  # 시작점을 중간점의 오른쪽으로 옮긴다

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search_reculsive(array, target, 0, n-1)   # 인덱스라서 n-1
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)  # result는 인덱스니까 하나 더해주기



# 반복문으로 구현한 이진 탐색 소스코드
def binary_search_repeat(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
    return None

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search_repeat(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)


## 탐색 범위가 2000만을 넘어가면 이진 탐색으로 접근해보자! O(logN)의 속도를 내는 알고리즘을 떠올려야 문제를 풀 수 있는 경우가 많다다