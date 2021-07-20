N = int(input())
M = int(input())


def findNum(n):
    if n == 1:
        return n
    elif n == 2:
        return -1

    else:
        for i in range(2, n // 2 + 1):
            if (n % i) == 0:
                return i
        return -1


sosu = []
for i in range(N, M + 1):
    if findNum(i) == -1:
        sosu.append(i)

if len(sosu) != 0:
    print(sum(sosu))
    print(sosu[0])
else:
    print(-1)
