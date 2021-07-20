### boj 1978: 소수 찾기
> 문제 주소: https://www.acmicpc.net/problem/1978


#### 문제 해결 방향
- 각각의 수가 소수인지 판별한다.
- 2 ~ 자기자신 // 2 인 수로 나누어 떨어지면 소수가 아니다. -> O(N)
- 2 ~ N의 제곱근까지 비교: O(logN) 
- 1은 소수가 아니고, 2는 소수이다.

```python
N = int(input())

# 숫자를 받아서 list 로 만든다.
num_list = list(map(int, input().split()))


def isPrime(p):
    # 1은 소수가 아니다.
    if p == 1: return False
    # 2는 소수이다.
    if p == 2: return True
    # 2 ~ N의 제곱근까지 비교
    # math.sqrt 함수 사용하면 run time error 발생하므로 주의 
    for j in range(2, int(p ** 1/2)+ 1):
        if p % j == 0: return False
    return True


count = 0
for i in num_list:
    if isPrime(i): count += 1

print(count)

```