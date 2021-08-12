'''
< 무지의 먹방 라이브 >
1번 음식부터 먹기 시작하고, 번호가 증가하는 순서대로 음식을 가져온다.
마지막 번호의 음식 섭취 후 다시 1번 음식이 온다.
음식 하나를 1초 동안 섭취한 후 다음 음식을 먹는다.
k초 후에 방송이 중단되었다. 몇 번 음식부터 섭취해야 하는지 알고자 한다.

food_times와 k가 주어진다. food_times 배열을 이용해야 하지 않을까.
solution : 네트워크 장애가 발생한 시간 k초가 매개변수로 주어질 때 몇 번 음식부터 다시 섭취하면 되는지 return하는 함수를 완성하라.

< 제한 사항 >
- food_times는 각 음식을 모두 먹는 데 필요한 시간이 음식의 번호 순서대로 들어 있는 배열
- k는 방송이 중단된 시간을 나타낸다.
- 더 섭취해야 할 음식이 없으면 -1 반환

< 정확성 테스트 제한 사항 >
- food_times의 길이는 1 이상 2000 이하
- food_times의 원소는 1 이상 1000 이하
- k는 1 이상 2000000 이하의 자연수

< 효율성 테스트 제한 사항 >
- food_times의 길이는 1 이상 200000 이하
- food_times의 원소는 1 이상 100000000 이하의 자연수
- k는 1 이상 2x10^13 이하의 자연수
'''

# 책 참고. 일일히 확인할 필요 없다! k를 최대한 줄인 다음에 확인하면 됨...
# 시간이 적게 걸리는 음식부터 확인한다. 우선순위 큐를 이용해 시간 기준 정렬 후 시간이 가장 적게 걸리는 음식을 다 먹을 때까지 걸리는 시간을 뺀다.

import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크다면
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.append(q, (food_times[i], i+1))

    sum_value = 0   # 먹기 위해 사용한 시간
    previous = 0    # 직전에 다 먹은 음식 시간
    length = len(food_times)    # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda  x:x[1])  # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]



# def solution(food_times, k):
#     answer = 0
#     while k != 0:
#         for i in range(len(food_times)):
#             if food_times[i] != 0:
#                 food_times[i] -= 1
#                 answer = i
#         if max(food_times) == 0:
#             answer = -1
#             break
#     return answer

