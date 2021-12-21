# boj 2805: 나무 자르기 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/2805
> 
> silver 3

## 나무 자르기
나무 M 미터가 필요. 절단기에 높이 H 지정. 나무를 필요한 만큼만 집으로 가져가려고 한다.

## 문제 해결 방향
책에서 나온 떡 자르기 문제랑 똑같다.
1. 원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제에 파라메트릭 서치(최적화 문제를 결정 문제로 바꾸어 해결하는 기법)를 사용한다.
2. **이런 파라메트릭 서치 문제 유형은 이진 탐색을 재귀적으로 표현하지 않고 반복문을 이용해 구현하면 더 간결하게 문제를 풀 수 있다.**
3. 이진 탐색을 이용해 잘라야 할 위치를 줄여가며 탐색한다.

```python
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
```
근데 이유를 모르겠지만 python3로 하면 타임아웃이 나오고 pypy3로 하면 타임아웃이 안나옴... 
다른 사람들 코드 찾아봐도 똑같이 했던데 이유를 모르겠음..!