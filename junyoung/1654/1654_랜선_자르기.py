import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = [int(input()) for _ in range(K)]
res = 0
s, e = 1, max(lan)

while e-s >= 0:
    num = 0
    mid = (s+e)//2
    for i in range(K):
        num += lan[i] // mid
    if num >= N:
        s = mid+1
    else:
        e = mid-1
    res = e
print(res)