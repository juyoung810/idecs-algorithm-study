# boj 2156 : 포도주 시식 
> 문제 주소: https://www.acmicpc.net/search#q=2156&c=Problems
> 
> 난이도: silver 1

## 1.문제설명
- 테이블위에 다양한 포도주들이 놓여져있음
- 포도주들의 양이 다 다름
- 최대로 포도주를 마시고싶음
- 하지만 3개의 포도주를 연속해서 마실수 없음

## 2.문제해결 아이디어.
- 계단오르기 문제랑 매우 유사하다
- 포도주의 총 갯수가 3개 이하라면 그냥 다 마시면됨
## 3.문제접근법
- 계단오르기와 똑같은 점화식을 쓰자! -> 틀림

## 4.특별히 참고할 사항
- 계단오르기는 계단을 무조건 올라야했지만(1칸 or 2칸), 포도주는 안마시고 넘어가도됨
```python
dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])
```
실제로 저 마지막항인 dp[i-1]을 안하면 예제 테스트케이스에서
```
[6, 16, 23, 28, 33, 32]
```
이렇게 그리드가 나옴
## 5.코드구현
``` python
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
dp = [0] * n
if n < 3:
    print(sum(arr))
else:
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2], dp[1])
    for i in range(3,n):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i], dp[i-1])
    print(dp[-1])
```