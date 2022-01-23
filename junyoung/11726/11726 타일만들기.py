import sys
input = sys.stdin.readline

n = int(input())
count = [[0 for i in range(n+1)] for j in range(2)]
count[0] = [1 for i in range(n+1)]
count[0][0] = count[1][0] = 0
for i in range(1, n+1):
    if i <2:
        count[1][i] = count[0][i]
    elif i ==2:
        count[1][i] = count[0][i] + 1
    else:
        count[1][i] = count[1][i-1] + count[1][i-2]
result = count[1][n] % 10007
print(result)

