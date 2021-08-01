# boj 2096 : 내려가기
> 문제 주소: https://www.acmicpc.net/problem/2096
> 
> 난이도: gold 4

## 1.문제설명
![img_5.png](img_5.png)

## 2.문제해결 아이디어.
- RGB거리랑 유사하다

## 3.문제접근법
_ RGB거리처럼 풀면됨
- 첫번째 row는 일단 pass
- 두번째 row부터 반복하며 이전 집의 색을 고려해 2가지 색의 경우의 비용을 고려

## 4.특별히 참고할 사항
- 메모리제한이 심하다.
- 현재 row는 이전 row의 값에만 영향을 받는다는걸 생각해야한다.
```python
min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]
```

## 5.코드구현
``` python
n = int(input())
min_dp = [[0] * 3 for _ in range(2)]
max_dp = [[0] * 3 for _ in range(2)]


for i in range(n):
    _temp = list(map(int, input().split()))

    max_dp[1][0] = _temp[0] + max(max_dp[0][0], max_dp[0][1])
    max_dp[1][1] = _temp[1] + max(max_dp[0][0], max_dp[0][1], max_dp[0][2])
    max_dp[1][2] = _temp[2] + max(max_dp[0][1], max_dp[0][2])

    min_dp[1][0] = _temp[0] + min(min_dp[0][0], min_dp[0][1])
    min_dp[1][1] = _temp[1] + min(min_dp[0][0], min_dp[0][1], min_dp[0][2])
    min_dp[1][2] = _temp[2] + min(min_dp[0][1], min_dp[0][2])

    max_dp[0][0], max_dp[0][1], max_dp[0][2] = max_dp[1][0], max_dp[1][1], max_dp[1][2]
    min_dp[0][0], min_dp[0][1], min_dp[0][2] = min_dp[1][0], min_dp[1][1], min_dp[1][2]

print(max(max_dp[1]), min(min_dp[1]))
```