n = int(input())
cache = [1e9] * (n+1)
cache[1] = 0 #1일 때
if n > 1:
    cache[2] = 1 #2일 때
if n > 2:
    cache[3] = 1 #3일 때

if n in [1,2,3]:
    print(cache[n])
    exit(0)
else:
    for i in range(4,n+1):
        if i%3 == 0 and i%2 == 0:
            cache[i] = min(cache[i-1], cache[i//3], cache[i//2]) + 1
        elif i%2 == 0 and i%3 != 0:
            cache[i] = min(cache[i-1], cache[i//2]) + 1
        elif i%2 != 0 and i%3 == 0:
            cache[i] = min(cache[i-1], cache[i//3]) + 1
        else:
            cache[i] = cache[i-1] + 1

print(cache[n])
