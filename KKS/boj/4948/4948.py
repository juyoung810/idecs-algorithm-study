import math
def finding_prime_sqrt(number):
    if number == 1:
        return False
    if number < 4:
        return True
    for x in range(2, int(math.sqrt(number))+1):
        if number%x == 0:
            return False
    return True

all_list = list(range(2,246912))
save_list = []

for i in all_list:
    if finding_prime_sqrt(i):
        save_list.append(i)



while True:
    num = int(input())
    if num == 0:
        break
    cnt = 0
    for i in save_list:
        if num < i <= num*2:
            cnt += 1
    print(cnt)



