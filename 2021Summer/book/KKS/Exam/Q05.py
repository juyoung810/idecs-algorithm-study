n, m = map(int, input())
data = list(map(int, input().split()))

array = [0] * 11
for x in data:
    array[x] += 1

result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i] * n

print(result)