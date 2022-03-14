import sys
input = sys.stdin.readline

N = int(input())
bud = list(map(int, input().split()))
M = int(input())
s, e = 0, max(bud)

while e-s >= 0:
    mid = (s+e)//2
    res = 0
    for i in range(N):
        if bud[i] >= mid:
            res += mid
        else:
            res += bud[i]
    if res > M:
        e = mid-1
    else:
        s = mid+1
print(e)

###########################################
import sys
input = sys.stdin.readline

N = int(input())
bud = list(map(int, input().split()))
M = int(input())
s, e = 0, max(bud)

while e-s >= 0:
    mid = (s+e)//2
    res = 0
    for i in bud:
        res += min(mid, i)
    if res > M:
        e = mid-1
    else:
        s = mid+1
print(e)

###########################################
# https://pacific-ocean.tistory.com/419

# import sys
# input = sys.stdin.readline
# n = int(input())
# s = list(map(int, input().split()))
# m = int(input())
# low, high = 0, max(s)
# while low <= high:
#     mid = (low + high) // 2
#     num = 0
#     for i in s:
#         if i >= mid:
#             num += mid
#         else: 
#             num += i
#     if num <= m: 
#         low = mid + 1
#     else: 
#         high = mid - 1
#     print(low, high)
# print(high)