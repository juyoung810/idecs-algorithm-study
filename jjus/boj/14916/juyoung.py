money = int(input())

five = money // 5
num = 0
for i in range(five, -1, -1):
    temp = money - 5 * i
    if temp % 2 == 0:
        num = temp // 2 + i
        break

if num != 0: print(num)
else: print(-1)

