'''
< 스티커 >
- 스티커 2n개가 있을 때, 스티커로 책상을 꾸민다.
- 스티커 한 장을 떼면 왼쪽, 오른쪽, 위, 아래에 있는 스티커는 사용할 수 없다.
- 뗄 수 있는 스티커의 점수의 최댓값을 구하라
'''

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(2)]
    if n == 2:
        max(d[0][1]+d[1][0], d[0][0]+d[1][1])
        continue
    elif n > 2:
        d[0][1] = d[0][1] + d[1][0]
        d[1][1] = d[1][1] + d[0][0]
        for i in range(2,n):
            d[0][i] = max(d[1][i-1], d[1][i-2]) + d[0][i]
            d[1][i] = max(d[0][i-1], d[0][i-2]) + d[1][i]
    print(max(d[0][n-1],d[1][n-1]))



# 왜 안되지..
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    d = [list(map(int, input().split())) for _ in range(2)]

    for i in range(1,n):
        if i == 1:
            d[0][i] += d[1][i-1]
            d[1][i] += d[0][i-1]
        else:
            d[0][i] += max(d[1][i-1], d[1][i-2])
            d[1][i] += max(d[0][i-1], d[0][i-2])

    print(max(d[0][n-1], d[1][n-1]))