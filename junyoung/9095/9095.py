import sys
input = sys.stdin.readline
N = int(input())
x_list= []
for _i in range(N):
    _x = int(input())
    x_list.append(_x)
x = 10
count = [[0 for i in range(x+1)] for j in range(3)]
count[0] = [0] + [1 for i in range(0, x+1)]
count[1][1] = count[2][1] = 1
for i in range(1, 3):
    for j in range(x+1):
        if i+1 > j:
            count[i][j] = count[i-1][j]
        elif i+1 == j:
            count[i][j] = count[i-1][j] +1
        else:
            _count = 0
            for _i in range(1, i+2):
                _count += count[i][j-_i]
            count[i][j] = _count
for _i in range(N):
    n = x_list[_i]
    print(count[2][n])