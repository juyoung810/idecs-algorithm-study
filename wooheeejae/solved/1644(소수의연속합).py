N = int(input())

# 에라토스테네스의 체
Num = [1] * (N + 1)
for i in range(2, N + 1):
    if Num[i]:
        t = 2
        while i * t <= N:
            Num[i * t] = 0
            t += 1

answer = 0
for i in range(N, 1, -1):
    if Num[i]:
        temp = 0
        for j in range(i, 1, -1):
            if Num[j]:
                temp += j
                if temp == N:
                    answer += 1
                    break
                elif temp > N:
                    break

print(answer)
