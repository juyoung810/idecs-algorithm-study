import sys
input = sys.stdin.readline
from bisect import bisect_left

N, M = map(int, input().split())
name = []
attack = []
for i in range(N):
    n, a = input().split()
    name.append(n)
    attack.append(int(a))
ch_at = [int(input()) for _ in range(M)]

for i in ch_at:
    s = bisect_left(attack, i)
    print(name[s])
    

###########################################
# 런타임 에러 (IndexError) 발생
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# name = []
# attack = [-1]
# for i in range(N):
#     n, a = input().strip().split()
#     a = int(a)
#     if a != attack[-1]:
#         name.append(n)
#         attack.append(int(a))
# del attack[0]

# ch_at = [int(input()) for _ in range(M)]

# def find_name(num):
#     s, e = 0, N-1
#     while e-s>=0:
#         mid = (s+e) //2
#         if num > attack[mid]:
#             s = mid +1
#         elif num < attack[mid]:
#             e = mid-1
#         else:
#             return mid
#     return e+1
    
# for i in ch_at:
#     _x = find_name(i)
#     print(name[_x])



###########################################
# 
# bisect 라이브러리의 bisect_left는 동일한 value가 존재하면 가장 왼쪽의 인덱스를 반환
# import sys
# import bisect

# input = sys.stdin.readline
# n, m = map(int, input().split())
# title = []
# power = [-1]
# for i in range(n):
#     t, p = map(str, input().rstrip().split())
#     title.append(t)
#     power.append(int(p))

# for _ in range(m):
#     p = int(input())
#     index = bisect.bisect_left(power, p)
#     print(title[index - 1])