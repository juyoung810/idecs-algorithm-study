import sys
input = sys.stdin.readline
    
N = int(input())
U = []
for _ in range(N):
    U.append(int(input()))

two = set() # a + b set
for i in range(N):
    for j in range(i,N):
        two.add(U[i] + U[j])

two_l = sorted(two) # set 정렬 -> 값 찾기 이분 탐색
U.sort() # U 정렬 -> 가장 큰 값 (i)- 가장 작은 값 (j) 부터 탐색
result = -1
for i in range(N-1,-1,-1):
    for j in range(0,N):
        k = U[i] - U[j] # U[a] + U[b] = U[i] - U[j]
        start = 0
        end = len(two_l) - 1
        while start <= end : 
            mid = (start + end) // 2
            if k == two_l[mid]: 
                result = U[i] # U[a] + U[b] + U[j] = U[i]
                break
            elif k > two_l[mid]:
                start = mid + 1
            else:
                end = mid -1

        if result != -1 : 
            break
    if result != -1 :
        break

print(result)
