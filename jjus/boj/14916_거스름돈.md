# boj 14916 거스름돈
> sivler 5
> https://www.acmicpc.net/problem/14916

## 1. 문제 설명
- 2, 5 원 존재
- 금액이 주어지고, 최소의 거스름돈 개수
- 불가할 경우 -1

## 2. 문제 해결 방향

- 최소의 동전 개수 이므로 5원을 우선으로 거슬러준다.
- 5월을 (주어진 돈) // 5 부터 0 개 까지 for 문을 돌리며
 주어진 금액에서 빼고, 남은 금액을 2월으로 나눌 수 있는 지 확인한다


## 3. 소스코드

1. 금액 입력받기, 최대 5원 갯수 구하기, 동전 갯수 초기화
```python

money = int(input())

five = money // 5
num = 0
```

2. 최대 5원 수 - 0 까지 확인하며, 남은 금액 2원으로 나눠지는지 확인
 동전의 갯수 갱신, 최소를 우선으로 확인하므로 바로 빠져나온다.

```python
for i in range(five, -1, -1):
    temp = money - 5 * i
    if temp % 2 == 0:
        num = temp // 2 + i
        break
```

3. 최종 갯수가 갱신 되지 않은 경우 -1 출력
```python
if num != 0: print(num)
else: print(-1)
```