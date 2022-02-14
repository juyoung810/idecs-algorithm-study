 # 기본 변수 설정
import sys
input = sys.stdin.readline

nat = int(input())
budNeed = list(map(int, input().split()))
budtotal = int(input())

 # 문제 풀이
def cal(N):
    temp = 0
    for i in budNeed:
        if N >= i:
            temp += i
        else:
            temp += N
    return budtotal - temp

start, end = 0, max(budNeed)
while start <= end:
    avg = (start + end) // 2
    if cal(avg) < 0:
        end = avg - 1
    else:
        start = avg + 1

print(end)
