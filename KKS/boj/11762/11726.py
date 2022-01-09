n = int(input()) # [1,1000]
cache = [1e9] * (1001)
# 2*n타일을 1*2, 2*1 타일로 채우는 방법
cache[1] = 1
cache[2] = 2
for i in range(3,1001):
    cache[i] = cache[i-2] + cache[i-1]
print(cache[n]%10007)