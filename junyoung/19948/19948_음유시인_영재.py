import sys
input = sys.stdin.readline

poem = input().strip().split()
space = int(input())
alpha = list(map(int, input().split()))
result = True

if len(poem)-1 > space:
    result = False
else:
    s = len(poem)
    for i in range(s):
        string_i = poem[i]
        for j in range(len(string_i)):
            num = ord(string_i[j].lower())-97
            alpha[num] -= 1
            if j>=1 and (string_i[j] == string_i[j-1]):
                alpha[num] += 1
            if alpha[num] <0:
                result = False
    if result == True:
        string = ''
        for i in range(s):
            string = string + poem[i][0].upper()
        for i in range(len(string)):
            num = ord(string[i].lower())-97
            alpha[num] -= 1
            if i>=1 and (string[i] == string[i-1]):
                alpha[num] += 1
            if alpha[num] <0:
                result = False
if result == True:
    print(string)
else:
    print(-1)