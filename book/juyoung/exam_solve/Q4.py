# 만들 수 없는 가장 작은 금액
# N개의 각각의 금액 주어짐
# 해당 합으로 만들 수 없는 가장 작은 금액

# 내 생각
# 최대 전체 합 + 1 크기의 배열 만든다.
# 반복문을 돌리며, 가장 큰 것 부터 시작해서 차례차례 해당 수를 만들 수 있는지 없는지 확인한다.

# 풀이
# 그리디 알고리즘 = 현재 상태에서 매번 가장 좋아 보이는 것만을 선택하는 알고리즘
# 현재 상태 = '1부터 target -1 까지의 모든 금액을 만들 수 있는 상태'
# 매번 target인 금액 만들 수 있는가 = 현재 확인하는 동전의 단위가 target 이하인지 확인
# 만들 수 있다면 target 값 없데이트 = 현재 상태 업데이트

import sys
input = sys.stdin.readline

# 동전의 개수 N 입력 받기
n = int(input())

# 동전 입력 받기
coins = list(map(int,input().split()))

### 내 생각
# # 동전을 내림 차순으로 정렬하기
# coins.sort(reverse= True)
#
# # 최소값 저장 위한 변수
# min_co = 0
#
# # money를 순회하며, 가장 큰 금액 부터 빼 가며 만들 수 있는지 확인
# for money in range(1,sum(coins)+1):
#     make = money
#     for coin in coins:
#         if coin <= make:
#             make -= coin
#             if make == 0:
#                 break
#     # 만들 수 없는 금액이면
#     if make != 0:
#         min_co = money
#         break

# # 주어진 금액의 합으로 1 ~ 금액합 까지 전부 만들 수 있다면, 금액합 +1 이 가장 작은 만들 수 없는 금액
# if min_co == 0:
#     print(sum(coins) +1)
# else:
#     print(min_co)

# coin을 오름 차순으로 정렬한다.
coins.sort()

# target = 1 부터 시작해서 만들 수 있는지 확인
target = 1
for coin in coins:
    # 만들 수 없는 금액 찾으면 반복 종료
    if target < coin:
        break
    # target이 2로 업데이트 된다 == 1까지 만들 수 있다.
    # target이 3보다 작다 == 1~ 1+1+2+3 까지의 금액은 다 만들 수 있다.
    target += coin


print(target)