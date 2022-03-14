 # 기본 변수 설정
N, M = map(int, input().split())
noHeard = set(input() for i in range(N))
noSeen = set(input() for i in range(M))

 # 문제 풀이
answer = sorted(list(noHeard & noSeen))
print(len(answer))
for n in answer:
    print(n)