'''

1. 내림차순 정렬

2. count = 3씩 저장하면서 , count = 2 일 경우 해당 묶음에서
가장 작은 수 이므로 더하지 않는다.

'''
import sys
input = sys.stdin.readline

N = int(input())

money = []
for _ in range(N):
    money.append(int(input()))

money.sort(reverse=True)

count = 0
result = 0
for i in range(N):
    if count != 2:
        result += money[i]
    if count == 3: count = 0
    count += 1

print(result)