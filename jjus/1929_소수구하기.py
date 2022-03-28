import sys
input = sys.stdin.readline

M,N = map(int,input().split())

isPrime = [True for _ in range(N+1)]
isPrime[0] = False
isPrime[1] = False
for i in range(2,N+1):
    if not isPrime[i]: continue
    j = 2*i
    while j <= N:
        isPrime[j] = False
        j += i



for num in range(M,N+1):
    if isPrime[num]:
        print(num)