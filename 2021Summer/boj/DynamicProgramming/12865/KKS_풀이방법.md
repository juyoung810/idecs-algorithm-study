# boj 12865 : 문제이름 by KKS
> 문제 주소: https://www.acmicpc.net/problem/12865
> 
> 난이도: gold 5

## 1.문제설명
가방에 물건의 가치가 가장 크게 넣고싶다 이때 가방의 가치는?

## 2.문제해결 아이디어.
- 2차원 배열을 통해 그리드를 만들고 접근

## 3.문제접근법
![img_3.png](img_3.png)
![img_4.png](img_4.png)
## 4.특별히 참고할 사항
- 물건을 나눠담을수 있으면 그리디
- 나눌수 없으면 dp로 풀면된다

## 5.코드구현
``` python
n, k = map(int, input().split())
value = []
weight = []
for i in range(n):
    w, v = map(int, input().split())
    value.append(v)
    weight.append(w)
dp = [[0]*(k+1) for _ in range(n+1)]
for i in range(n+1):
    for w in range(k+1):
        if i == 0 or w == 0:
            dp[i][w] = 0
        elif weight[i-1] <= w: #가방에 담을수 있다면
            #행에 해당하는 물건의 가치와 남는 공간에 넣을수 있는 가치를 합한것과
            #기존물건을 그대로 가져가는 경우의 가치를 비교한다.
            dp[i][w] = max(value[i-1] + dp[i-1][w-weight[i-1]], dp[i-1][w])
        else:
            #안들어가면 기존물건 그대로 가져감
            dp[i][w] = dp[i-1][w]
print(dp[n][k])
```