N = int(input())

price = []
for i in range(0,N):
    x = int(input())
    price.append(x)
pay = 0
price.sort()
while len(price) >= 3:
    x1 = int(price.pop())
    x2 = int(price.pop())
    x3 = int(price.pop())
    pay = pay + x1 + x2
for i in range(0, len(price)):
    pay = pay + int(price[i])

print(pay)