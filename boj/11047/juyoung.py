import sys

N,K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

count = 0
while K > 0:
    coin = coins.pop()
    if K // coin != 0:
        count += K // coin
        K = K % coin

sys.stdout.write(str(count))