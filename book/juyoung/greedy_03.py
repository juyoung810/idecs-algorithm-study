N,K = map(int,input().split())

# N % K 만큼 -1 하면 N 이 K의 배수가 된다.
# N이 무조건 K 보다 크거나 같으므로, 계속 빼기만 하는 경우는 없다.

# count = 0
# while N > 1:
#    if N % K != 0:
#        count += N % K
#        N = N - (N%K)
#    else:
#        count += 1
#        N = N // K

### 최대한 많이 K로 나눈다. ####### 그리디 생각하기
count = 0
while N >= K :
    if N % K != 0:
        N -= 1
        count += 1
    else:
        N //= K
        count += 1

while N > 1:
    N -= 1
    count+=1

print(count)