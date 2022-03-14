'''
< 가장 큰 증가 부분 순열 >
- 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중 합이 가장 큰 것을 구하는 프로그램을 작성하라

< 아이디어 >
- 수열의 값을 비교해서 더 작으면 값을 더한다.
'''

import sys
input = sys.stdin.readline

n = int(input().rstrip())
a = list(map(int, input().split()))
d = [0] * n

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += a[i]

print(max(d))