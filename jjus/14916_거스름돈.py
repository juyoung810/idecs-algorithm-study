"""
1. 문제 설명
- 2, 5 원 존재
- 금액이 주어지고, 최소의 거스름돈 개수
- 불가할 경우 -1

2. 문제 해결 방향

- 최소의 동전 개수 이므로 5원을 우선으로 거슬러준다.
- 5월을 (주어진 돈) // 5 부터 0 개 까지 for 문을 돌리며
 주어진 금액에서 빼고, 남은 금액을 2월으로 나눌 수 있는 지 확인한다
- 최소의 경우 부터 확인했으므로 조건을 만족할 경우 바로 답이 된다.

"""

money = int(input())

five = money // 5
num = 0
for i in range(five, -1, -1):
    temp = money - 5 * i
    if temp % 2 == 0:
        num = temp // 2 + i
        break

if num != 0: print(num)
else: print(-1)

