import sys

input = sys.stdin.readline

# 두 수의 차이가 목표보다 크거나 같을 경우 작은 수를 더 크게 -> 차이 줄어들도록
# 두 수의 차이가 목표보다 작을 경우 큰 수를 더 크게 -> 차이를 더 크게
def two_pointer(a, n, m):
    s = 0
    e = 0
    result = 2e9 # 가능한 가장 큰 수
    while s <= e < n and s >= 0:
        t = a[e] - a[s]
        if t >= m:
            if result > t:
                result = t
            s += 1
        else:
            e += 1
    return result




N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

# 양 끝 포인터를 움직이기 위해 정렬
arr.sort()
print(two_pointer(arr, N, M))
