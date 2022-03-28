'''
< 소수 구하기 >
- M 이상 N 이하의 소수를 모두 출력하는 프로그램을 작성하시오

< 아이디어 >
- 에라토스테네스의 체
1. 찾고자 하는 범위의 자연수 나열
2. 1을 지운다
3. 2의 배수를 지운다
4. 다음 소수의 배수를 모두 지운다

n의 제곱근까지 검사하면 된다.

'''

import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def isPrime(m, n):
    prime = [True] * (n+1)
    for i in range(2, int((n+1)**0.5)+1):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    for i in range(m, n+1):
        if prime[i]:
            print(i)

isPrime(M, N)



# 다른 코드
import sys
input = sys.stdin.readline

M, N = map(int, input().split())

def isPrime(num):
    if num == 1:
        return False
    else:
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True

for i in range(M, N+1):
    if isPrime(i):
        print(i)