# 두 배열의 원소 교체

# N개의 원소가지는 두 배열, K 번 바꿔치기 가능
N,K = map(int,input().split())


A = list(map(int,input().split()))
B = list(map(int,input().split()))

# A의 가장 작은 원소 3개와 , B의 가장 큰 원소 3개를 swap 해야한다.
# A는 오름차순 정렬
# B는 내림차순 정렬
A = sorted(A)
B = sorted(B,reverse=True)

# print(A)
# print(B)
for i in range(K):
    if A[i] < B[i]:
        A[i],B[i] = B[i],A[i]
    else: break # A의 원소가 같거나 크면 그 뒤도 마찬가지 이므로 break

# print(A)
# print(B)

print(sum(A))