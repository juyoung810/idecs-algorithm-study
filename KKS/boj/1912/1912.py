N = int(input())
numbers = list(map(int, input().split()))
cache = [-1000] * (N)
cache[0] = numbers[0]
for i in range(1,N):
    #cache[i] = i번째 숫자까지 연속된 최대합
    cache[i] = max(numbers[i], numbers[i] + cache[i-1])
print(max(cache))