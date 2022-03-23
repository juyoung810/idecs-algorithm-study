import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int,input().rstrip().split()))

count = 0

def prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

for n in nums:
    if prime(n):
        count += 1
print(count)