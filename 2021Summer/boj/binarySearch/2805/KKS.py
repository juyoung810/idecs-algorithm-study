import sys
input = sys.stdin.readline
n, m = map(int, input().split())
data = list(map(int,input().split()))

low = 0
high = max(data)

result = 0
while low <= high:
    total = 0
    mid = (low + high)//2
    for item in data:
        if item > mid:
            total += (item-mid)
    if total < m:
        high = mid - 1
    else:
        result = mid
        low = mid+1
print(result)