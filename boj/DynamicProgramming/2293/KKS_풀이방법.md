# boj 2293 : 동전1
> 문제 주소: https://www.acmicpc.net/problem/2293
> 
> 난이도: silver 1

## 1.문제설명
n가지 종류의 동전이 있다. 각각의 동전이 나타내는 가치는 다르다. 이 동전을 적당히 사용해서, 그 가치의 합이 k원이 되도록 하고 싶다. 그 경우의 수를 구하시오. 각각의 동전은 몇 개라도 사용할 수 있다.

사용한 동전의 구성이 같은데, 순서만 다른 것은 같은 경우이다.

## 2.문제해결 아이디어.
- 처음에 2차원 배열로 하려다 잘 안되기도 할꺼같고, 메모리가 작아서 pass
- 숫자를 만들려고하는 숫자만큼의 1차원 배열을 만들자 (0~k) 까지
```python
dp = [0 for _ in range(k+1)]
dp[0] = 1
```
만들려고하는 숫자가 0 일때는 방법이 무조건 1개임

## 3.문제접근법
``` 
for i in coin:
    for j in range(i,k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]
```
- 2중 for문 사용
- 가지고있는 동전과 특정수를 비교해서 / 특정 수 보다 동전이 크면 차만큼의 dp값을 더해줌
- 이전 행의 n원을 만들 수 있는 경우의 수와 n원에서 현재 동전의 가치 k원를 뺀 가치의 경우의 수의 합

## 4.특별히 참고할 사항
- 메모리제한 4mb, 1차원리스트에 덮어쓰면서 진행해야됨.

## 5.코드구현
``` python
n, k = map(int, input().split())
coin = []
for i in range(n):
    coin.append(int(input()))
dp = [0 for _ in range(k+1)]

dp[0] = 1
for i in coin:
    for j in range(i,k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[k])
```