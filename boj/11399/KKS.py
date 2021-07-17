n = int(input())
data = list(map(int, input().split()))
data.sort()
for i in range(1,len(data)):
    data[i] = data[i-1] + data[i]
print(sum(data))
