### 떡볶이 떡 만들기
## 길이가 일정하지 않은 떡의 길이를 절단기로 잘라서 맞춰준다!
## 손님이 왔을 때 요청한 총 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하라

## 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 파라메트릭 서치(최적화 문제를 결정 문제로 바꾸어 해결하는 기법)를 사용한다.
## 이런 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 표현하지 않고 반복문을 이용해 구현하면 더 간결하게 문제를 풀 수 있다.

n, m = list(map(int, input().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, input().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in array:
        # 잘랐을 때의 떡의 양 계산
        if x > mid:
            total += x - mid
    # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
    if total < m:
        end = mid - 1
    # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
    else:
        result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

# 정답 출력
print(result)