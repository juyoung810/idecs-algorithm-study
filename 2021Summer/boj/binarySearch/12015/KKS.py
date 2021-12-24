import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int,input().split()))
lis = []
def search_index(lis, x):
    start = 0
    end = len(lis) -1
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] < x:
            start = mid + 1
        else:
            end = mid - 1
    return start


for item in arr:
    if not lis or lis[-1] < item:
        lis.append(item)
    else:
        idx = search_index(lis, item)
        lis[idx] = item

print(len(lis))