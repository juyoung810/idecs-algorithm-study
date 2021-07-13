# N = int(input())
#
# count = 0
# while N > 0:
#     if N >= 500:
#         N -= 500
#         count+=1
#     elif N >= 100:
#         N -= 100
#         count+=1
#     elif N >= 50:
#         N -= 50
#         count+=1
#     elif N >= 10:
#         N -= 10
#         count+=1
#
# print(count)

## O(N) -> 하나씩 빼므로 너무 오래 걸린다.

N = int(input())
count = 0

coins = [500,100,50,10]

for coin in coins:
    count += N // coin
    N %= coin

print(count)

## O(K) -> K: 화폐의 종류 수 (N보다 훨씬 감소한다.)

