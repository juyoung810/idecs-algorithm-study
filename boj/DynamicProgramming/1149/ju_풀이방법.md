# boj 1149: RGB거리 
> 문제 주소: https://www.acmicpc.net/problem/1149
> 
> silver 1


## 문제 해결 방법

- 필요한 숫자: 이전 dp 값, 현재 입력된 집의 rgb 비용
- 각각 일차원 배열로 만들어, 메모리 낭비를 줄인다.
- rgb 값을 이전 dp에 저장한 값으로 지정하고, 
  rgb 값 + 해당 색과 같지 않은 다음 색 했을 때 이전에 저장된 dp 값보다 작으면 저장한다.
- 이전 값을 변수에 저장하고, dp 값을 update해서 계속 비교하기 위해, 문제에서 구할 수 있는 최댓값으로 dp 값을 초기화 해서
작을 때 update 할 수 있도록 한다.
- r: 1,2 를 다음 색으로 칠할 수 있다.
- g: 0,2를 다음 색으로 칠할 수 있다.
- b: 0,1를 다음 색으로 칠할 수 있다.
```python
# dp = N * 3 행렬로 만든다.
# 입력 받은 rgb는 일차원 행렬로 그때 그때 받는다.

import sys

n = int(sys.stdin.readline())
# n*3 행렬 만들어 1001로 초기화한다.
dp = []


for i in range(n):
    rgb = list(map(int,sys.stdin.readline().split()))
    # 초기화 해주기
    if i == 0:
        dp.append(rgb[0])
        dp.append(rgb[1])
        dp.append(rgb[2])

    # 각각의 값 비교해서 update
    else:
        # 이전값을 더해서 비교하기위해
        r = dp[0]
        g = dp[1]
        b = dp[2]

        # 최초로 더할때, 가장 큰 1000 * n +1 보다 작은 값으로 해야한다.
        dp[0] = 1000 * n + 1
        dp[1] = 1000 * n + 1
        dp[2] = 1000 * n + 1

        # r 
        if dp[1] > r + rgb[1]: dp[1] = r + rgb[1]
        if dp[2] > r + rgb[2]: dp[2] = r + rgb[2]
        # g
        if dp[0] > g + rgb[0]: dp[0] = g + rgb[0]
        if dp[2] > g + rgb[2]: dp[2] = g + rgb[2]
        # b
        if dp[0] > b + rgb[0]: dp[0] = b + rgb[0]
        if dp[1] > b + rgb[1]: dp[1] = b + rgb[1]

sys.stdout.write(str(min(dp)))
```

#### 간과한 점
- 가장 큰 수를 지정할 때 모든 경우를 고려하지 않아 `1000 * n +1`로 지정하지 않았다.
- 해당 경우 1000개의 집이 1000일 때, update 되지 않는 것을 알 수 있다.