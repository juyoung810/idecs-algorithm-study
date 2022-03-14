'''
< IF문 좀 대신 써줘 >

- 캐릭터가 가진 전투력을 기준으로 칭호를 붙인다.
- 칭호의 개수와 캐릭터 개수가 주어질 때, 캐릭터의 전투력에 맞는 칭호를 입력 순서대로 출력.
- 어떤 캐릭터의 전투력으로 출력할 수 있는 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력

< 아이디어 >
- 얘를 이진탐색으로 어떻게 풀지,,,,,,,,,,,
- 칭호를 리스트로 받아서 인덱스로 푼다. 어디 사이에 넣으면 될지 생각해본다.

< 다른 방법 >
- bisect 패키지의 bisect_left를 이용한다.
- bisect : 이진 탐색 쉽게 구현해주는 함수
- bisect_left(literable, value) : 왼쪽 인덱스 구하기, right는 오른쪽 인덱스 구하기

'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
names = [input().split() for i in range(n)]

def bs(li,p):
    s, e = 0, len(li)-1
    res = 0
    while s <= e:
        mid = (s+e) // 2
        if int(li[mid][1]) >= p:
            e = mid-1
            res = mid
        else:
            s = mid + 1
    return res

for i in range(m):
    p = int(input())
    print(names[bs(names,p)][0])



# bisect로 해보기
import sys
input = sys.stdin.readline
from bisect import bisect_left

n, m =map(int, input().split())
title = []
power = []

for i in range(n):
    N, P = input().split()
    title.append(N)
    power.append(int(P))

for i in range(m):
    p = int(input())
    print(title[bisect_left(power, p)])