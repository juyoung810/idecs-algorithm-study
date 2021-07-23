N = int(input())

money = []
for _ in range(N):
    in_num = int(input())
    if in_num == 0:
        money.pop()
    else:
        money.append(in_num)

print(sum(money))