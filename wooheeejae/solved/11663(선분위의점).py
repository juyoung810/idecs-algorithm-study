 # 기본 변수 설정
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N, M = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
line = []
for i in range(M):
    line.append(list(map(int, input().split())))

for j in range(M):
    start = bisect_left(point, line[j][0])
    end = bisect_right(point, line[j][1])
    print(end - start)

#
# poiN, linN = map(int, input().split())
# poi = list(map(int, input().split()))
# poi.sort()
# lin = []
# for i in range(linN):
#     lin.append(list(map(int, input().split())))
#
#  # 문제 풀이
# def calStart(i):
#     start, end = 0, poiN-1
#     while start <= end:
#         avg = (start + end) // 2
#         if lin[i][0] <= poi[avg] <= lin[i][1]:
#             end = avg -1
#         else:
#             if poi[avg] < lin[i][0]:
#                 start = avg + 1
#             elif poi[avg] < lin[i][0]:
#                 end = avg - 1
#     return avg
#
# def calEnd(i):
#     start, end = 0, poiN-1
#     while start <= end:
#         avg = (start + end) // 2
#         if lin[i][0] <= poi[avg] <= lin[i][1]:
#             start = avg + 1
#         else:
#             if poi[avg] < lin[i][0]:
#                 start = avg + 1
#             elif poi[avg] < lin[i][0]:
#                 end = avg - 1
#     return avg
#
# for j in range(linN):
#     if poi[calStart(j)] >= lin[j][0] and poi[calEnd(j)] <= lin[j][1]:
#         print(calEnd(j) - calStart(j) + 1)
#     elif poi[calStart(j)] < lin[j][0] and poi[calEnd(j)] > lin[j][1]:
#         print(calEnd(j) - calStart(j) - 1)
#     else:
#         print(calEnd(j) - calStart(j))
