
import sys

input = sys.stdin.readline

N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))

m = price[0]
res = 0
for i in range(N - 1):
    if price[i] < m:
        m = price[i]
    res += m * road[i]

print(res)
