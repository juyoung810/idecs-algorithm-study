import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
line = [list(map(int, input().split())) for _ in range(M)]
for i in range(len(line)):
    s = bisect_left(point, line[i][0])
    e = bisect_right(point, line[i][1])
    print(e-s)