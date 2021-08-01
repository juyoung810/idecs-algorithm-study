# boj 11053 : 가장 긴 증가하는 부분수열
> 문제 주소: https://www.acmicpc.net/problem/11053
> 
> 난이도: silver 2

## 1.문제설명
- 가장 긴 증가하는 부분 수열의 길이를 찾아라

## 2.문제해결 아이디어.
- 1차원 그리드를 생성해서 풀어보자
- 이중 for문으로 피벗을 잡고, 피벗 이전의 값과 비교해서 피벗의 값이 더 크면
- 그리드를 비교해보자

## 3.문제접근법
아래가 핵심코드
```python
for i in range(1,n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
```

## 4.특별히 참고할 사항
- 딱히 없음
- 시간복잡도는 O(N^2)

## 5.코드구현
``` python
n = int(input())
data = list(map(int,input().split()))
dp = [1] * n

for i in range(1,n):
    for j in range(i):
        if data[j] < data[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(dp)
print(max(dp))
```