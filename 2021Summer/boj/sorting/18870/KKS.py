import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
data2 = list(sorted(set(data)))
dic = {value : index for index, value in enumerate(data2)}

for item in data:
    print(dic[item], end = ' ')