# [가방 무게, 보석 가격] 저장
# 들어갈 수 있는 무게가 작은 가방 부터 집어 넣는다. -> 가방 무게 작은 순 정렬 필요
# 가방에 넣을 수 있는 것들 : 가방 무게 이하인 것들 중, 돈이 큰 것 부터 집어 넣고, list에서 제외 시킨다.
# 가방 배열을 만들어서 무게가 작은 순으로 정렬한다.
# 보석 (value, 무게) 를 담는 배열을 만들어서 무게를 기준으로 오름 차순 정렬한다.
# 가방이 갯수만큼 반복문을 돌리며, 해당 가방이 넣을 수 있는 보석의 무게에 해당하는 것들을 우선 순위 큐에 넣는다.
# 우선 순위 큐는 돈을 기준으로 MaxHeap이 만들어지므로, 가장 위에 있는 것을 가방에 넣고 큐에서 삭제한다.


# 파이썬 priority Queue: from queue import PriorityQueue
# Queue.put() -> get() 할 때는 오름 차순으로 나온다.
# O(log N)

from queue import PriorityQueue
import sys
N, K = map(int, sys.stdin.readline().split())
jewels = []
bags = []

# 보석 받아서,
for _ in range(N):
    jewels.append(tuple(map(int, sys.stdin.readline().split())))

for _ in range(K):
    bags.append(int(sys.stdin.readline()))

# 보석 무게 오름차순 정렬
jewels.sort(key=lambda x: x[0])
# 가방 무게 오름차순 정렬
bags.sort()
sum = 0
# jewel은 한 바퀴만 돌 수 있도록 한다.
# 가방이 무게 순으로 정렬되어 있으니, pq 에 담겨 있는 무게들 당연히 넣을 수 있으므로
jewel_idx = 0
pq = PriorityQueue(N)
# 가방의 수 만큼 반복한다.
for i in range(K):
    while jewel_idx < N and jewels[jewel_idx][0] <= bags[i]:
        # 가방의 무게보다 보석의 무게가 작거나 같으면 , max PQ에 넣기
        pq.put(-jewels[jewel_idx][1])
        jewel_idx += 1

    if not pq.empty():
        sum += -pq.get()

sys.stdout.write(str(sum))
