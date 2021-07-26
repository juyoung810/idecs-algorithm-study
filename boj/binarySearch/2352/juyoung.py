#LIS 를 통해 풀 수 있다.
import sys
n = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().rstrip().split()))


def binarySearch(lis,target):
    start = 0
    end = len(lis) -1
    while start <= end:
        mid = (start + end) // 2
        if lis[mid] == target:
            return mid
        elif lis[mid] > target:
            end = mid -1
        else: start = mid +1

    return start

lis = []
for arr in array:
    # lis 가 비어있을 경우
    if not lis:
        lis.append(arr)
    else:
        if arr > lis[len(lis) -1]:
            lis.append(arr)
        else:
            idx = binarySearch(lis, arr)
            lis[idx] = arr

print(lis)
sys.stdout.write(str(len(lis)))