# https://www.acmicpc.net/problem/20300
# n = list(map(int, input().split()))

import sys
input = sys.stdin.readline
N = int(input())
n = list(map(int, input().split()))
n.sort()
if N %2 ==0:
    M = n[0]+n[-1]
    for i in range(N//2):
        M = max(M, n[i]+n[-1-i])
else:
    M = n[-1]
    for i in range(N//2):
        M = max(M, n[i]+n[-2-i])
print(M)

#####################################################
# 시행착오(오류)
# import sys
# input = sys.stdin.readline
# N = int(input())
# x = list(map(int, input().split()))
# x.sort()
# if N %2 ==0:
#     m = x[0] + x[-1]
#     for i in range(1, N//2):
#         _m = x[i] + x[N-1-i]
#         if _m < m:
#             m = _m
# else:
#     m = x[-1]
#     for i in range((N-1)//2):
#         _m = x[i]+x[N-2-i]
#         if _m < m:
#             m = _m
# print(m)

####################################################
# 정답
# N = int(input())
# M = list(map(int, input().split()))
# M = sorted(M)

# if N % 2 != 0:
#     M.pop()

# ans = 0
# for i in range(N//2):
#     ans = max(ans,  M[i] + M[-1-i])

# print(ans)