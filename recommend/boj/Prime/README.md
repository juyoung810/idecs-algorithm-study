# 소수 (prime)
> 소수: 약수가 1과 자기 자신 밖에 없는 수

소수 알고리즘 2가지

1. 어떤 수 N이 소수인지 아닌지 판별하는 방법
2. N 보다 작거나 같은 모든 자연수 중에서 소수를 찾아내는 방법(범위 내)

## 1. 어떤 수 하나에 대해서 판별

1. 2보다 크거나 같고 n-1 보다 작거나 같은 수로 나누어 떨어지면 소수가 아니다.

    시간 복잡도 : O(N)

1. 2보다 크거나 같고, N/2 보다 작거나 같은 자연수로 나누어 떨어지면 안된다.

    시간 복잡도: O(N)

2. 제곱근 이용

    N = a*b

    a < = b , a와 b가 차이가 가장 작은 경우는 루트  N이다. 따라서 루트 N 까지만 검사하면 된다.

    시간 복잡도: O(루트 N)

## 2. N이하의 소수 마다 루트N까지 검사한다. (범위의 수)

1. 제곱근 까지 판별 

    시간 복잡도: O(N루트N)

####  2. 에라토스테네스의 체

   #####  N 이하 다  뿌려넣고 존재하는 가장 작은 소수의 배수를 지워나간다.

    지워지지 않은 수 중에서 가장 작은 수는 2이다. 2는 소수이니까 2의 배수를 다 지운다.(2*2 - 2*50)

    그 다음으로 3은 소수이므로 3의 배수 다 지운다.(3*3 - 3*50) 

     ( 4는 2의 배수이므로 다 지워진다.)

    지워지지 않은 수 중 가장 작은 수 5는 소수이므로 5의 배수를 다 지운다. (5*5 - 지워진다)

    그 다음 7의 배수를 다 지운다.(7*7 - 지워진다.)

   ##### → 자기 자신의 제곱 수 보다 작은 것은 지워진것이 보장된다.

    따라서 11 부터는 배수를 지우지 않아도 된다. (11*10 이하는 다 지워지는 것이 보장되므로)→ 남은 건 다 소수