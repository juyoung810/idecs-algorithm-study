'''
< 선분 위의 점 >
- 일차원 좌표상의 점 N개와 선분 M개가 주어진다.
- 각각의 선분 위에 입력으로 주어진 점이 몇 개 있는지 구하는 프로그램을 작성하시오

< 입력 >
1. 점의 개수 N, 선분의 개수 M
2. 점의 좌표
3~M. 선분의 시작점과 끝점

< 아이디어 >
- 이진분류를 어떻게 이용할까?
- 받은 점들에 대해 리스트를 생성한다.
- 선분의 시작점과 끝점의 인덱스를 찾는다.
- 인덱스값을 바탕으로 사이에 점이 몇개 있는지 구한다.
'''

import sys
input = sys.stdin.readline
from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
dots = list(map(int, input().split()))
dots.sort()

for _ in range(M):
    s, e = map(int, input().split())
    sidx = bisect_left(dots, s)
    eidx = bisect_right(dots, e)
    print(eidx-sidx)