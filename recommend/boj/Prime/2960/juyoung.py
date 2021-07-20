N,K = map(int, input().split())

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


print(find_prim(prime_num,K))

