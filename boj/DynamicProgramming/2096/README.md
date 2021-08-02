# boj 2096: 내려가기 by juyoung
> 문제 주소: https://www.acmicpc.net/problem/2096
> 
> gold 4

## 문제 해결 방법
- __메모리 제한이 큰 문제다.__
- N은 100,000 까지이고, 3*N 까지 배열을 입력 받으면 4MB를 이미 초과한다.
- N차원 배열의 입력과, dp table를 생성하지 않는다.  
- 1차원 배열을 이용해 __입력 받음과 동시에 dp table를 계산한다.__
- 필요한 건 이전의 상태(dp에 계산됨), 와 현재 row(그때 그때 입력받음)이다.
### 소스코드
1. dp table을 이차원 배열로 생성한다. 
- 0 row: max_dp 
- 1 row: min_dp
```python
N = int(sys.stdin.readline())
# 현재 줄, 다음 줄만 저장한다.
dp = [[0,0,0],[9,9,9]]
```
2. i == 0 즉, 첫번째 row를 입력 받을 경우, dp에 값을 그대로 update 해준다.
```python
for i in range(N):
    down = list(map(int,sys.stdin.readline().split()))
    if i == 0:
        for j in range(3):
            dp[0][j] = down[j]
            dp[1][j] = down[j]
...
```
3. 첫번째 row가 아닐 경우, 기존의 dp 값과 입력 받은 값을 조건에 맞게 계산해 update 한다.
- max: 입력 받은 값 + max(비교해야하는 cell)
- min: 입력 받은 값 + min(비교해야하는 cell)
```python
 else:
        # 최대 구하기
        a = dp[0][0]
        b = dp[0][1]
        c = dp[0][2]

        dp[0][0] = down[0] + max(a, b)
        # column 1 일 때
        dp[0][1] = down[1] + max(a, b, c)
        # column 2 일 때
        dp[0][2] = down[2] + max(b, c)

        # 최소 구하기
        a = dp[1][0]
        b = dp[1][1]
        c = dp[1][2]

        # column 0 일 때
        dp[1][0] = down[0] + min(a, b)
        # column 1 일 때
        dp[1][1] = down[1] + min(a, b, c)
        # column 2 일 때
        dp[1][2] = down[2] + min(b, c)

```
4. 출력
- max: dp의 0번째 행에서 가장 큰 값
- min: dp의 1번째 행에서 가장 작은 값
```python
print(max(dp[0]),min(dp[1]))
```