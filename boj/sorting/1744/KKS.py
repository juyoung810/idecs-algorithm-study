import sys
input = sys.stdin.readline
n = int(input())
positive = []
negative = []
result = 0

for _ in range(n):
    value = int(input())

    if value>1:
        positive.append(value)
    elif value == 1: #처음에 여기서 실수 1은 곱하는거보단 더하는게 더 커짐
        result += 1
    else:
        negative.append(value)

positive.sort(reverse=True) #큰수부터
negative.sort() #작은수부터

if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        result += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        result += positive[i] * positive[i + 1]
    result += positive[len(positive)-1]

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        result += negative[i] * negative[i + 1]
    result += negative[len(negative)-1]

print(result)