## boj 2609 : 최대 공약수와 최소 공배수
> 주소: https://www.acmicpc.net/problem/2609


### 문제 해결 방향
+ 최대공약수: 두 수가 들어오면 더 작은 수로 큰 수를 나누는 것을 반복해서, 둘 중 하나라도 0이 된다면 0이 아닌 다른 수가 최대공약수가 된다.

ex) if a < b : gcd(a,b % a)
    else a >= b: gcd(a % b, a)

+ 최소공배수: 각각의 수를 최대 공약수로 나눈 몫과 최소 공약수를 곱한다.

####-> 분석 후

두 수의 크기에 상관하지 않고, 무조건 다른 한 수가 0이 될 때 까지 과정을 반복한다고 생각하고 재귀적으로 반복
(더 큰 수로 나누더라도 똑같이 더 작은 수가 나머지로 나와서 반복되므로)

    def gcd(a, b):
    if b != 0: return gcd(b,a%b)
    else: return a

    a, b = map(int, input().split())

    gcd_num = gcd(a, b)
    lcm_num = gcd_num*(a // gcd_num) * (b // gcd_num)
    print(gcd_num)
    print(lcm_num)