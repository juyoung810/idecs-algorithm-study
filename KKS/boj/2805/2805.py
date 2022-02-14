N, M = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)

ans = 0
while low <= high:
    total = 0
    mid = (low + high) // 2
    for tree in trees:
        if tree > mid:
            total += tree-mid
    if total < M:
        high = mid - 1
    else:
        ans = mid
        low = mid + 1

print(ans)


