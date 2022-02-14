'''
< 랜선 자르기 >
- N개의 랜선 만들기
- K개의 랜선을 잘라서 같은 길이의 N개의 랜선 만들기
- N개보다 많이 만드는 것도 N개 만드는 것에 포함
- 만들 수 있는 최대 랜선의 길이를 구하라

< 아이디어 >
- 이진탐색으로 구현한다.
- 나무 자르는 것과 유사하게 중간값으로 계속 자른다.
- 잘라진 값이 자르는 값보다 크면 반복한다. 재귀?
- 잘라진 개수의 합이 n보다 작거나 크면 중간값을 변경한다.
'''

import sys
input = sys.stdin.readline
from collections import deque

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    cut = deque()
    result = 0
    for line in lan:
        result += line // mid

    if result < n:
        end = mid - 1
    else:
        start = mid + 1

print(end)