# <span style="color:red">boj 9465: 스티커 by juyoung </span>
> 문제 주소: https://www.acmicpc.net/problem/9465
> 
> silver 2


## 문제 해결 방향
- 2차원 행렬로 스티커의 값을 저장한다.
- 0번째 column의 dp 값은 해당 스티커 값 그대로 이다.
- 1번째 column의 dp 값은 왼쪽 대각선 값과 해당 cell의 값의 합이다.
- 2번째 column 부터는 
    1. 0번째 row: [1][0] + [0][2] VS [1][1] + [0][2] 의 값을 비교해서 최대가 되는 것을 해당 dp 값으로 저장한다.
    2. 1번째 row: [0][0] + [1][2] VS [0][1] + [1][2] 의 값을 비교해서 최대가 되는 것을 해당 dp 값으로 저장한다.
    
- 이렇게 반복해서, 마지막 column에서 둘 중 최대 값이 스티커 값의 최대가 된다.

#### 그림 참고
![boj9465](./img/ju_boj9465.png)
- 주황색, 초록색 두 값을 비교한다.
- 초록색과 더한 값이 더 크면 30,100을 선택하는 것이다.
- 주황색과 더한 값이 더 크면 50,50,100을 선택하는 것이다.


#### 소스코드
1. 이차원 행렬로 입력 받고, 각 cell에 최댓값 저장 위해 dp table 또한 이차원 행렬로 생성
```python
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    N = int(sys.stdin.readline())
    stickers = []
    # 스티커 점수 입력 받기
    stickers.append(list(map(int,sys.stdin.readline().split())))
    stickers.append(list(map(int, sys.stdin.readline().split())))

    # 각 경우 최댓값 기록 위한 dp table 생성
    dp = []
    dp.append([0] * N)
    dp.append([0] * N)

```
2. column N-1까지 순환하며 dp table를 채운다.
- 0, 1은 따로 계산해준다.
```python
 for i in range(N):
        # column 0 초기화
        if i == 0:
            dp[0][0] = stickers[0][0]
            dp[1][0] = stickers[1][0]
        # column 1 초기화
        elif i == 1:
            dp[0][1] = dp[1][0] + stickers[0][1]
            dp[1][1] = dp[0][0] + stickers[1][1]
        # row  비교 후 update
        else:
            if dp[1][i-2] + stickers[0][i] >= dp[1][i-1] + stickers[0][i]:
                dp[0][i] = dp[1][i-2] + stickers[0][i]
            else: dp[0][i] = dp[1][i-1] + stickers[0][i]

            # row 1 비교 후 update
            if dp[0][i-2] + stickers[1][i] >= dp[0][i-1] + stickers[1][i]:
                dp[1][i] = dp[0][i-2] + stickers[1][i]
            else: dp[1][i] = dp[0][i-1] + stickers[1][i]


   

```
3. 마지막 column의 값 중 더 큰 값이 최댓값이다.
```python
 sys.stdout.write(str(max(dp[0][N-1],dp[1][N-1])) + "\n")
```
   

