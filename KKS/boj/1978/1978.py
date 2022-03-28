import math
def finding_prime_sqrt(number):
    num = abs(number)
    if num == 1:
        return False
    if number < 4:
        return True
    for x in range(2, int(math.sqrt(num))+1):
        if num%x == 0:
            return False
    return True

N = int(input())
num_list = map(int,input().split())
cnt = 0
for item in num_list:
    if finding_prime_sqrt(item):
        cnt+=1
print(cnt)