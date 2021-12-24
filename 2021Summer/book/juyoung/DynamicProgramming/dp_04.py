
N,M = map(int,input().split())

# N개의 화폐 단위 정보 입력받기
array = []
for _ in range(N):
    array.append(int(input()))

d = [10001] * (M + 1) # 1 ~ M 까지 값 저장 위해

d[0] =  0
for i in range(N):
    for j in range(array[i],M+1):
        if d[j - array[i]] != 10001 : #(i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j],d[j-array[i]] + 1)


if d[M] == 10001:
    print(-1)
else: print(d[M])

