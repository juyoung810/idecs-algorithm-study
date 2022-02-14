'''
< 퇴사 2 >
- n+1 일째 되는 날 퇴사를 위해 n일동안 최대한 많은 상담을 하려고 함
- 하루에 하나씩 서로 다른 사람의 상담 잡음
- 각각의 상담은 완료까지 걸리는 기간 Ti와 받을 수 있는 금액 Pi로 이루어져 있다.
- 상담을 적절히 했을 때, 최대 수익을 구하는 프로그램을 작성하라

< 아이디어 >
- 1일부터 가능한 날을
'''

import sys
input = sys.stdin.readline

n = int(input())
Ti = []
Pi = []
d = [0] * n

for _ in range(n):
    t, p = map(int, input().split())
    Ti.append(t)
    Pi.append(p)

for i in range(n):
    if i+Ti[i] > n:
        continue
    d[i] += Pi[i]
    d[i+Ti[i]] = max(d[i+Ti[i]],d[i])

print(max(d))