'''
< 사다리 >
- 길이가 x인 사다리와 y인 사다리가 땅에서부터 정확히 c인 지점에서 서로 교차한다.
- 두 빌딩은 얼마나 떨어져 있을까?

 < 아이디어 >
 - 닮음비를 이용하면 교차지점의 높이에 대한 식을 구할 수 있다.
 - h = h1h1/(h1+h2)
 - 이진탐색을 이용해 h와 c가 교차하는 지점의 d를 구한다.
'''

import sys
input = sys.stdin.readline
import math

x, y, c = map(float, input().split())
left, right = 0, min(x,y)

while (abs(left-right) > 1e-6):
    mid = (left + right) / 2
    d = mid
    h1 = math.sqrt(float(x**2 - d**2))
    h2 = math.sqrt(float(y**2 - d**2))
    h = (h1*h2)/(h1+h2)
    if h > c:
        left = d
    else:
        right = d


print("%.3f"%round(mid,3))
