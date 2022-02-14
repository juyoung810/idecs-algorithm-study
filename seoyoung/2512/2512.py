'''
< 예산 >

- 국가예산의 총액이 정해져 있다. 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같은 방법으로 배정
1. 모든 요청이 배정될 수 있는 경우 요청한 금액 그대로 배정
2. 모든 요청 배정될 수 없는 경우 특정한 정수 상한액 계산하여 그 이상인 예산요청에는 모두 상한액 배정. 상한액 이하의 예산요청에 대해서는 요청한 금액 그대로 배정

< 아이디어 >
- 이진 탐색을 이용한다.
- 중간값으로 계속 자른다. 넘으면 줄이고, 안넘으면 최댓값을 저장한다.
'''

import sys
input = sys.stdin.readline

n = int(input())
cities = list(map(int, input().split()))
m = int(input())

# if sum(cities) <= m:
#     print(max(cities))
#     sys.exit(0)

start = 0
end = max(cities)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for city in cities:
        if city >= mid:
            result += mid
        else:
            result += city

    if result > m:
        end = mid - 1
    else:
        start = mid + 1

print(end)