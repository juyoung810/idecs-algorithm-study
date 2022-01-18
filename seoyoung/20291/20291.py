'''
< 파일 정리 >
- 파일을 확장자 별로 정리해서 몇 개씩 있는지 알려주기
- 보기 편하게 확장자들을 사전 순으로 정렬하기!
=> 노트북 파일 정리를 해줄 프로그램 만들기

< 아이디어 >
1. '.' 기준으로 스플릿해서 확장자만 저장
2. 딕셔너리를 만들어서 구한다!
'''

import sys
input = sys.stdin.readline

n = int(input())
names = dict()
for _ in range(n):
    extend = (input().split('.'))[1]
    if extend in names:
        names[extend] += 1
    else:
        names[extend] = 1

sort_names = sorted(names.items())
for key, value in sort_names:
    print(key.rstrip(), value)


# Counter 사용
import sys
input = sys.stdin.readline
from collections import Counter

n = int(input())
names = []
for _ in range(n):
    names.append((input().split('.'))[1])

sort_names = Counter(names)
sort_names = sorted(sort_names.items())
for key, value in sort_names:
    print(key.rstrip(), value)