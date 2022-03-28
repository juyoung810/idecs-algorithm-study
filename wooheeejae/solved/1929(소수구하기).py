import math

N, M = map(int, input().split())

for i in range(N, M+1):
    if i == 1:
        continue
    elif i < 4:
        print(i)
        continue
    else:
        for j in range(2, int(math.sqrt(i)+1)):
            if i % j == 0: # 소수가 아님
                break
            if j == int(math.sqrt(i)+1)-1:
                print(i)