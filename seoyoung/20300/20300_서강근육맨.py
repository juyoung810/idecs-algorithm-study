'''
pt를 한번 받을 때 운동기구를 최대 두개까지 선택 가능
N개의 운동기구를 한 번씩 사용하고 싶다.
pt를 한 번 받을 때의 근손실 정도가 M을 넘지 않도록 하고 싶다.
M의 최소값은?

< 아이디어 >
1. 짝수인 경우 - 큰 값과 작은 값끼리 더한다. 제일 큰 값이 M
2. 홀수인 경우 - 제일 큰 값을 제외하고 나머지끼리 더한다. 제일 큰 값이 M
'''

import sys
input = sys.stdin.readline

n = int(input())
equips = list(map(int, input().split()))
equips.sort()
result = 0

if n % 2 == 0:
    for i in range(n//2):
        result = max(equips[i] + equips[n-1-i], result)
else:
    result = equips[-1]
    for i in range((n-1)//2):
        result = max(equips[i] + equips[n-2-i], result)

print(result)
