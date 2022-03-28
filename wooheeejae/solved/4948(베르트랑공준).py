import math

while True:
    N = int(input())
    if N == 0:
        break
    answer = 0
    for i in range(N+1, 2*N+1):
        if i == 1:
            continue
        elif i < 4:
            answer += 1
            continue
        else:
            for j in range(2, int(math.sqrt(i) + 1)):
                if i % j == 0:  # 소수가 아님
                    break
                if j == int(math.sqrt(i) + 1) - 1:
                    answer += 1
    print(answer)
