##############################################
# 오류
# import sys
# input = sys.stdin.readline

# N = int(input())
# data = [[0]*(N+1) for _ in range(3)]
# for i in range(1, N+1):
#     _x, _y = map(int, input().split())
#     data[0][i] = i
#     data[1][i] = i+_x-1
#     data[2][i] = _y
# profit = [0] *(N+1)

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         start = data[0][j]
#         end = data[1][j]

#         if i>=start and M <= N:
#             profit[i] = max(profit[start-1]+data[2][j], profit[i])
# print(profit)



############################################## 
# 시간 초과 오류
# import sys
# input = sys.stdin.readline

# N = int(input())
# data = [[0] *N for _ in range(3)]
# dp = [0] *N
# for i in range(N):
#     data[0][i], data[1][i] = map(int, input().split())
#     data[2][i] = i + data[0][i]
#     if i == 0:
#         dp[i] = data[1][i]
#     else:
#         if data[2][i] <= N:
#             M=0
#             for j in range(i):
#                 if i >= data[2][j]:
#                     M = max(dp[j], M)
#             dp[i] = M + data[1][i]
#         else:
#             dp[i]=dp[i-1]
# print(max(dp))

#############################################
# https://dndi117.tistory.com/entry/aaa
# import sys 
# input = sys.stdin.readline 

# n = int(input())
# t,p = [],[]
# dp = [0] * (n+1)
# for i in range(n):
#     x,y = map(int,input().split())
#     t.append(x)
#     p.append(y)
# M = 0 
# for i in range(n):
#     M = max(M,dp[i])  
#     if i+t[i] > n :  
#         continue 
#     dp[i+t[i]] = max(M+p[i],dp[i+t[i]])
# print(max(dp))