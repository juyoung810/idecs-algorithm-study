import sys
import math
input = sys.stdin.readline

T = int(input())

def my_sum(n):
    result = 0
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            if n // i == i:
                result += i
            else:
                result += n // i
                result += i

    print(result)


for _ in range(T):
    N = int(input())
    my_sum(N)
