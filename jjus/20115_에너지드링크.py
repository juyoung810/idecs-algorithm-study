"""
1. 가장 큰 것을 기준으로 정렬 -> 큰 것에 모두 넣는다.
2. 나누기 할 때 실수로 나눠줘야 소수점까지 나온다.
128ms
"""
import sys

input = sys.stdin.readline

N = int(input())

drinks = list(map(int, input().rstrip().split()))

drinks.sort(reverse=True)
result = drinks[0]

for i in range(1, N):
    result += drinks[i] / 2

print(result)
