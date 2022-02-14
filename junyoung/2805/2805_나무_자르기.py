import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))
s, e = 1, max(height)

while e-s >=0:
    mid = (s+e)//2
    tree = 0
    for i in height:
        tree += max(i-mid, 0)
    if tree >= M:
        s = mid +1
    else:
        e = mid -1
print(e)

#################################################
# Pyhon3에서는 시간초과 발생 => PyPy3에서는 잘 돌아감

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))
start, end = 0, max(height)

while end >= start:
    mid = (start+end)//2
    tree = 0
    for i in height:
        if i > mid:
            tree += (i-mid)
    if tree >= M:
        start = mid+1
    else:
        end = mid-1
print(end)

#################################################

import sys
input = sys.stdin.readline

N, M = map(int,input().split()) 
trees = list(map(int, input().split()))

start, end = 0, max(trees) 

while start <= end:
    mid = (start+end)//2
    tree = 0 
    for i in trees:
        if i > mid: 
            tree += i - mid

    if tree >= M: 
        start = mid + 1
    else:
        end = mid - 1
print(end)