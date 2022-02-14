 # 기본 변수 설정
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tit = []
for i in range(N):
    tit.append(input().split())
    if len(tit) > 1:
        if tit[-1][1] == tit[-2][1]:
            del tit[-1]

 # 문제 풀이
for i in range(M):
    cha = int(input())
    start, end = 0, len(tit) - 1
    while start <= end:
        avg = (start + end) // 2
        if int(tit[avg][1]) >= cha:
            end = avg - 1
        else:
            start = avg + 1
    print(tit[end + 1][0])

