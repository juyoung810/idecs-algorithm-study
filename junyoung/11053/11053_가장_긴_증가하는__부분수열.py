import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

count = [1] * N
for i in range(1, N):
    _list = []
    for j in range(i):
        if A[i] > A[j]:
            _list.append(j)
    if len(_list) ==0:
        count[i] = 1
    else:
        _x = count[_list[0]]
        for _i in range(len(_list)):
            index = _list[_i]
            _x = max(count[index], _x)
        count[i] = _x+1
    print(_list)
M = max(count[i] for i in range(N))
print(M)


