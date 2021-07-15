import time
n, k = map(int,input().split())
start_t = time.time()
cnt = 0
while n > 1:
    if n%k == 0:
        n = n//k
    else:
        n -= 1
    cnt += 1
print(cnt)
end_t = time.time()
print("time :" , end_t - start_t)