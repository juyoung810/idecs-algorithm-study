# https://www.acmicpc.net/problem/20300
# n = list(map(int, input().split()))

import sys
input = sys.stdin.readline
N = int(input())
x = list(map(int, input().split()))
x.sort()
if N %2 ==0:
    m = x[0] + x[-1]
    for i in range(1, N//2):
        _m = x[i] + x[N-1-i]
        if _m < m:
            m = _m
else:
    m = x[-1]
    for i in range((N-1)//2):
        _m = x[i]+x[N-2-i]
        if _m < m:
            m = _m
print(m)                
                            
####################################################
# N = int(input())
# n = input().split()
# x = list(map(int, n))
# x.sort()
# M = float("inf")
# if N %2 ==0:
#     for i in range(int(N/2)):
#         M = min(M, x[i]+x[N-1-i])
# else:
#     N = N-1
#     for i in range(int(N/2)):
#         M = min(M, x[i]+x[N-1-i])
#     if x[N] < M:
#         M = x[N]
        
# print(M)

####################################################

# N = int(input())
# M = list(map(int, input().split()))
# M = sorted(M)

# if N % 2 != 0:
#     M.pop()

# ans = 0
# for i in range(N//2):
#     ans = max(ans,  M[i] + M[-1-i])

# print(ans)



####################################################
# import sys
# input = sys.stdin.readline

# n = int(input())
# equips = list(map(int, input().split()))
# equips.sort()
# result = 0

# if n % 2 == 0:
#     for i in range(n//2):
#         result = max(equips[i] + equips[n-1-i], result)
# else:
#     result = equips[-1]
#     for i in range((n-1)//2):
#         result = max(equips[i] + equips[n-2-i], result)

# print(result)