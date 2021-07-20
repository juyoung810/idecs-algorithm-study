### boj 2960: 에라토스테네스의 체
> 문제 주소 : https://www.acmicpc.net/problem/2960

#### 문제 해결 방향
- 2 - N 까지의 숫자 리스트를 생성한다.
- 리스트에서 가장 작은 소수의 배수를 삭제한다.
- 해당하는 소수의 배수의 시작은 소수의 제곱 수 부터이다.
- 소수의 제곱수  ~ 소수* N//소수 까지 돌면서 존재하는 배수를 찾아 삭제한다.
- 제곱 수 이전의 수들은 이미 다른 소수의 배수여서 다 삭제되었다.

```python
# 2 ~ N까지의 list만든다.
prime_num = [i for i in range(2,N+1)]


def find_prim(prime_num,K):
    count = 0
    while count < K:
        # 현재 리스트에 존재하는 가장 작은 소수를 뽑는다.
        p = prime_num.pop(0)
        key = p
        count += 1
        if count == K: return(key)
        # 해당 소수의 배수가 list 에 존재한다면 제외시킨다.
        # 해당 소수의 배수가 존재하는지 확인
        temp = N // p
        # 존재하는 가장 작은 소수의 배수는 제곱 수 부터 시작이다.
        # 이전의 수는 다 지워졌다.
        if temp != 0:
            for i in range(p, temp + 1):
                # 배수가 아직 리스트에 존재한다면 삭제
                if prime_num.count(p * i) != 0:
                    key = prime_num.pop(prime_num.index(p * i))
                    count += 1
                    if count == K: return(key)


```