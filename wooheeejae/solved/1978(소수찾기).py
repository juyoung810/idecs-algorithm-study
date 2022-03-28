import math

N = int(input())
answer = 0
isPN = list(map(int, input().split()))

for j in isPN:
    if j == 1:
        continue
    elif j < 4:
        answer += 1
        continue
    else:
        for k in range(2, int(math.sqrt(j)+1)):
            if j % k == 0: # 소수가 아님
                break
            if k == int(math.sqrt(j)+1)-1:
                answer += 1

print(answer)