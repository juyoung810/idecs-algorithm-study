n, m = map(int, input().split())
array = list(map(int, input().split()))

low = 0
max = max(array)

result = 0
while low <= max:
    total = 0
    mid = (low + max)//2
    for x in array:
        if x > mid:
            total += (x - mid)
    if total < m:
        max = mid-1
    else:
        result = mid
        start = mid + 1
print(result)