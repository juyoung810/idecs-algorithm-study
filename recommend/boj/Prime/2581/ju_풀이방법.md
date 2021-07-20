### boj 2581: 소수
> 문제주소 : https://www.acmicpc.net/problem/2581

### 문제 해결 방향
#### 소수란 무엇인가? 1과 자기 자신만을 약수로 갖는 수
1. 1이면 소수가 아니다.

2. 2는 소수이다.

3. [2 ~ 자신/2 의 수] 중에 자신과 나누어 떨어지는 수가 없으면 소수이다.


```
N = int(input())
M = int(input())


def findNum(n):
    if n == 1:
        return n
    elif n == 2:
        return -1

    else:
        # 2부터 자기 자신 /2 까지의 수와 나눠서 나누어 떨어지는지 검증
        for i in range(2, n // 2 + 1):
            if (n % i) == 0:
                return i
        return -1


sosu = []
for i in range(N, M + 1):
    if findNum(i) == -1:
        ## 소수인 경우 list에 더한다.
        sosu.append(i)

if len(sosu) != 0:
    print(sum(sosu))
    # 리스트는 인덱싱 가능
    print(sosu[0])
else:
    print(-1)


```