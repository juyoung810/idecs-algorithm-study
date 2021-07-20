import math

N = int(input())

num_list = list(map(int, input().split()))


def isPrime(p):
    if p == 1: return False
    if p == 2: return True
    for j in range(2, int(p ** 1/2) +1 ):
        if p % j == 0: return False
    return True


count = 0
for i in num_list:
    if isPrime(i): count += 1

print(count)
