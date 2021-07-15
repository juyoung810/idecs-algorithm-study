m, n = map(int, input().split())
result = 0
for i in range(n):
    row = list(map(int, input().split()))
    min_value = min(row)
    result = max(min_value, result)
print(result)