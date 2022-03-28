import sys
import math
input = sys.stdin.readline

limit = 123456
prime = [True] * (2 * limit + 1)
prime[0] = False
prime[1] = False
def isPrime():
    for i in range(2, int(math.sqrt(len(prime)))):
        if not prime[i]: continue
        for j in range(i+i, len(prime), i):
            prime[j] = False


isPrime()
N = int(input())
while N != 0 :
    print(prime[N+1:2*N+1].count(True))
    N = int(input())
