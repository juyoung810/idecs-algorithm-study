n = int(input())

prime_tf = [False, False] + [True] * (n-1)
prime_nums = []

for i in range(2, n+1):
    if prime_tf[i]:
        prime_nums.append(i)
        for j in range(2*i, n+1, i):
            prime_tf[j] = False

result = 0
start = 0
end = 0

while end <= len(prime_nums):
    temp = sum(prime_nums[start:end])
    if temp == n:
        result += 1
        end += 1
    elif temp < n:
        end += 1
    else:
        start += 1

print(result)