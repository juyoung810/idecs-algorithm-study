"""
두 입력의 중복 구하기
- set 통해 입력 받고 intersection(교집합) 구하기

1. s1.intersection(s2)
2. s1 & s2

- 결과 list 로 변경 후 sort
- 길이 출력 & list 요소 출력

"""
import sys
input = sys.stdin.readline

N,M = map(int,input().split())

listen = set()
see = set()
for _ in range(N):
    listen.add(input().rstrip())

for _ in range(M):
    see.add(input().rstrip())

#result = list(listen.intersection(see))
result = list(listen & see)
result.sort()
print(len(result))
for r in result:
    print(r)
