### 가장 긴 증가하는 부분 수열
## 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하라

n = int(input())
array = list(map(int, input().split()))

d = [0] * n

for i in range(n):
    for j in range(i):
        if array[i] > array[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1

print(max(d))