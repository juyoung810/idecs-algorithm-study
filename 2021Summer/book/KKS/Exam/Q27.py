def binary_search_start(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            if mid - 1 < 0 or arr[mid - 1] != target:
                return mid
            else:
                end = mid - 1
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def binary_search_end(arr, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            if mid + 1 >= len(arr) or arr[mid + 1] != target:
                return mid
            else:
                start = mid + 1
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

N, x = map(int, input().split())
arr = list(map(int, input().split()))

if binary_search_start(arr, x, 0, N-1) == -1 :
        print(-1)
else:
    print(binary_search_end(arr, x, 0, N-1) - binary_search_start(arr, x, 0, N-1) + 1)