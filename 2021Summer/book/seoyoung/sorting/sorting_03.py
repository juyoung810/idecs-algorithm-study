### 두 배열의 원소 교체
## 최대 k 번의 바꿔치기 연산 수행 가능. 배열 A의 모든 원소의 합이 최대가 되도록 하자!
## 배열 A에서 가장 작은 원소를 골라서 배열 B의 가장 큰 원소와 교체하기!

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()  # 배열 A는 오름차순 정렬 수행
B.sort(reverse=True)  # 배열 B는 내림차순 정렬 수행

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 k번 비교
for i in range(k):
    # A의 원소가 B의 원소보다 작은 경우
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]
    else: # 나머지 경우
        break

print(sum(A))