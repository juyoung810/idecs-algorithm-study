import math
m, n = map(int, input().split())

def finding_prime_sqrt(number):
    if number == 1:
        return
    if number < 4:
        return print(number)
    for x in range(2, int(math.sqrt(number))+1):
        if number%x == 0:
            return
    return print(number)

for i in range(m, n+1):
    finding_prime_sqrt(i)