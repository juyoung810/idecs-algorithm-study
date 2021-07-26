### 나무 자르기
## 나무 M 미터가 필요. 절단기에 높이 H 지정. 나무를 필요한 만큼만 집으로 가져가려고 한다.
## 책에서 나온 떡 자르기 문제랑 똑같음

import sys

# 입력받고
n, m = map(int, sys.stdin.readline().split())
# 나무 길이 저장 받고
trees = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(trees)
H = 0

# 반복문으로 이진탐색 구현
while start <= end:
    total = 0
    mid = (start + end) // 2
    # 잘라서 total 구하기.
    for x in trees:
        # 나무가 더 긴 경우 자르기
        if x > mid:
            total += x - mid
    # total이 부족한 경우 더 많이 자르기(왼쪽으로 이동)
    if total < m:
        end = mid - 1
    # total이 많은 경우 덜 자르기(오른쪽으로 이동)
    else:
        H = mid  # 최대한 덜 잘라야 하니까 기록
        start = mid + 1

print(H)
