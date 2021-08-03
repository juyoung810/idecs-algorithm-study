# boj 2156: 포도주 시식 by seoyoung
> 문제 주소: https://www.acmicpc.net/problem/2156
> 
> silver 1

## 문제
연속으로 놓여 있는 3잔을 마실 수 없는 상황에서, 주어진 포도주를 가장 많이 마실 수 있는 양을 구하라.
책에 나온 두번째 예제와 비슷한 문제이다.

## 문제 해결 방향
규칙을 발견해 점화식을 잘 세우는 것이 중요! 직접 해보고 규칙을 찾아야 하는 듯 하다.
![alt text]()

## 소스코드

```python
n = int(input())
wine = []

for i in range(n):
    wine.append(int(input()))

d = [0] * n

if n == 1:
    print(wine[0])
elif n == 2:
    print(sum(wine))
else:
    d[0] = wine[0]
    d[1] = d[0] + wine[1]
    d[2] = max(d[1], d[0] + wine[2], wine[1] + wine[2])

    for j in range(3, n):
        d[j] = max(d[j-1], d[j-2] + wine[j], d[j-3] + wine[j-1] + wine[j])

    print(d[n-1])
```