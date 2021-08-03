# boj 11053: 가장 긴 증가하는 부분 수열 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/11053
> 
> silver 2

## 문제
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램 작성

## 문제 해결 방향
수열의 길이와 같은 배열을 생성해 현재 위치 이전에 더 작은 원소의 개수를 저장한다.

## 소스코드

```python
n = int(input())
array = list(map(int, input().split()))

d = [0] * n
```
수열의 각 원소에 대해, 해당 위치 이전의 모든 원소와 비교한다.
해당 위치의 원소가 더 크고, 생성한 배열의 같은 인덱스의 값이 비교하는 원소 인덱스의 값보다 작다면 같게 만든 후, 1을 더한다.
배열에서 가장 큰 값을 출력해 가장 긴 증가하는 부분 수열의 길이를 출력한다.
```python
for i in range(n):
    for j in range(i):
        if array[i] > array[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))
```