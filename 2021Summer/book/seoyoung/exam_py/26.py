'''
## 카드 정렬하기
> 문제 주소 : https://www.acmicpc.net/problem/1715

### 1. 문제
N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지 구하는 프로그램을 작성하라.

### 2. 문제 해결 방향
- 숫자 묶음이 있을 때, 큰 단위의 비교를 최대한 적게 해야 한다.
- 작은 수의 카드끼리 비교해 큰 묶음을 만든다.
- 새로운 묶음을 만든 후 매번 새로 정렬해 작은 두개끼리 더한다.
- 매번 새로 정렬하는건 귀찮다! 경식오빠가 얘기해주신대로 힙을 써서 최소인 걸 뽑아낸다.
'''

import heapq

n = int(input())
h = []

for _ in range(n):
    heapq.heappush(h, int(input()))

result = 0

while h:
    new = 0
    new += heapq.heappop(h)
    if h == []:
        break

    new += heapq.heappop(h)

    result += new
    heapq.heappush(h, new)

print(result)