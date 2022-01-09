'''
1. 많이 주는 사람이 먼저 계산하도록 정렬 -> 내림차순 정렬
2. index 만큼 tip 빼고 준다.
112ms -> enumerate
'''
import sys

input = sys.stdin.readline

N = int(input())

tips = []
for i in range(N):
    tips.append(int(input()))

tips.sort(reverse = True)

money = 0
for i in range(N):
    if tips[i] - i > 0:
        money += tips[i] - i

print(money)

