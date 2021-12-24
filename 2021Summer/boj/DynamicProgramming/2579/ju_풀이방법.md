# <span style = "color:red">boj 2579: 계단 오르기 by
> 문제 주소: https://www.acmicpc.net/problem/2579
> 
> silver 3


## 문제 해결 방향
- 점화식 세우는 방법 몰랐음
- dp에 n까지 있을 경우의 최댓값 저장한다 생각
1. 1개 있으면 그게 최댓값
2. 2개 있으면 두개 더한게 최댓값
3. 3개 있으면 
    1. 0->2 밟은 경우
    2. 1->2 밟은 경우
    
    둘 중 최댓값
4. 3개 이상 있으면
    1. 마지막 전 칸 밟은 경우 -> dp[i-3]: 마지막 경로 + stairs[i-1]:마지막 칸 + stairs[i] : 해당 칸 이다.
    2. 마지막 전 칸 안 밟은 경우 -> dp[i-2]: 마지막 경로 + stairs[i] : 해당 칸
    
    둘 중 최댓값


```python
p[0] = stairs[0]
if n > 1:
    dp[1] = stairs[0] + stairs[1]
if n > 2:
    # 3번째 칸은
    # 1. 0->2
    # 2. 1-> 2
    dp[2] = max(stairs[0]+stairs[2],stairs[1]+stairs[2])
if n > 3:
    for i in range(3,n):
        # 1. 마지막 계단의 전 계단을 밟은 경우 n = 4 0->2->4
        # 2. 마지막 계단의 전 계단을 밟지 않은 경우
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3],stairs[i] + dp[i-2])
```