'''
< 동전 0 >
N 종류의 동전의 합이 K가 되는 동전의 최소 갯수?
n, k 가 주어지고, 둘째줄부터 동전의 종류가 오름차순으로 주어진다.
k보다 작은 화폐 단위들 중 가장 큰 것부터 차근차근 채운다! 나누기 반복
'''

n, k = map(int, input().split())

coins = []
for i in range(n):
    coins.append(int(input()))
coins.reverse()

result = k
cnt = 0

for coin in coins:
    if coin < k:
        cnt += result // coin
        result %= coin

print(cnt)