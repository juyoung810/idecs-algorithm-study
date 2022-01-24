'''
< 듣보잡 >
- 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램 작성

< 입력 >
n = 듣도 못한 사람의 수, m = 보도 못한 사람의 수
듣도 못한 사람의 이름, 보도 못한 사람의 이름
듣보잡의 수와 그 명단을 사전순으로 출력하기

< 아이디어 >
- set으로 저장한다.
- 듣도 못한 사람의 이름을 먼저 저장한다.
- 보도 못한 사람이 듣도 못한 사람에 포함되면 결과에 추가한다.
- 결과를 sort해서 출력한다.
'''

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
hear = set()
dbj = []

for _ in range(n):
    name = input()
    hear.add(name)

for _ in range(m):
    name = input()
    if name in hear:
        dbj.append(name)

dbj.sort()
print(len(dbj))
for name in dbj:
    print(name.rstrip())