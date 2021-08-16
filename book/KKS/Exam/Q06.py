import heapq


def solution(food_times, k):
    answer = -1
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i + 1))
    food_num = len(food_times)  # 남은음식
    previous = 0  # 이전 타임에 제거한 음식 food_time

    while h:
        t = (h[0][0] - previous) * food_num  # 남은양 * 남은음식 갯수
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(h)
            food_num -= 1
        else:
            idx = k % food_num
            h.sort(key=lambda x: x[1])
            answer = h[idx][1]
            break
    return answer