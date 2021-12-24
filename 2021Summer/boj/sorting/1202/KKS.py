import sys
import heapq
input = sys.stdin.readline
from collections import deque
#보석의 총 개수 N, 가방의 총 개수 K
n , k = map(int, input().split())
arr = []
ruck = []
for i in range(n):
    #무게, 가격 입력
    arr.append(list(map(int, input().split())))
for i in range(k):
    #가방마다 담을수 있는 무게
    ruck.append(int(input()))


arr = deque(sorted(arr, key = lambda x : x[0]))
print(arr)
heap = []
ruck.sort()

value = 0
for weight in ruck:
    while arr and weight >= arr[0][0]:
        heapq.heappush(heap, -arr.popleft()[1]) #무게를 주는데 가장 작은값이 첫번째 인덱스에 위치해서 -붙혀줌
    if heap:
        value -= heapq.heappop(heap)
print(value)
