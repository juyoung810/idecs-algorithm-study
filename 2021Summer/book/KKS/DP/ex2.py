n = int(input())
array = list(map(int, input().split()))

d = [0] * 100
# d에는 원하는 값이 들어있음, 인덱스- 몇번째 원소까지
d[0] = array[0]
d[1] = max(array[0],array[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1]) #인덱스랑 맞춰주려고