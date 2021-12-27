import heapq
ans = 0
n = int(input())
ropes = []
for i in range(n):
    heapq.heappush(ropes, int(input()))

for i in range(n):
    if ropes[0] * n > ans:
        ans = ropes[0] * n
    heapq.heappop(ropes)
    n -= 1

print(ans)