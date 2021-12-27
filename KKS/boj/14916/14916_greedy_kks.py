n = int(input())

ans = 0
num = n%5
if n == 1 or n == 3:
    print(-1)
    exit(0)

elif num%2 == 0:
    print(n//5 + num//2)

else:
    print((n//5)-1 + (num+5)//2)
    exit(0)
