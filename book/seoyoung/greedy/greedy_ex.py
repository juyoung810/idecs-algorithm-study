# 예제 3-1) 거스름돈

import time
start_time = time.time()

n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin

print(count)

end_time = time.time()
print("time :", end_time - start_time)