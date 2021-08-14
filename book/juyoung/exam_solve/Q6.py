
import heapq
def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 적은 순 정렬
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q ,(food_times[i] , i +1))

    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times)

    # key point : 가장 시간이 적은 음식을 기준으로 계산하면, 시간이 더 걸리는 음식도 자연스럽게 계산할 수 있다.
    # sum_value + (현재 음식의 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    # 현재 까지 남은 가장 작은 음식을 먹는 데 까지 걸린 시간이 K 보다 크면, 그 음식을 다 먹지 못하고, 남은 것 중 하나 차례에 중단되는 것
    # 이전 음식 시간 빼는 이유 -> 이전 음식 시간 계산할 때, 같이 시간이 -1 됐을 것 이므로
    while sum_value +(q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중 (k - 이전 음식 다 먹은 시간 ) 번째 음식 고르기
    result = sorted(q,key=lambda x:x[1])
    return result[(k-sum_value) % length][1]

k = int(input())
food_times = list(map(int,input().split()))

print(solution(food_times,k))