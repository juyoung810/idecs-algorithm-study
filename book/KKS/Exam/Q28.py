def binary_search(nums, start, end):
    while start <= end:
        mid = (start + end)//2
        if mid == nums[mid]:
            return mid
        elif mid >= nums[mid]:
            start = mid + 1
        else:
            end = mid -1
    return -1



import sys
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

print(binary_search(nums, 0, N-1))