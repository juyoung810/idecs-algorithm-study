
n,k = map(int,input().split())
array = []
for _ in range(n):
    array.append(int(input()))


d = [0] * 100001

for i in range(n):
    d[array[i]] = d[array[i]] + 1
    for j in range(array[i] + 1,k+1):
        if d[j-array[i]] != 0:
            d[j] = d[j] + d[j-array[i]]


print(d[k])