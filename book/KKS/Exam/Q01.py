import sys
input = sys.stdin.readline


n = int(input())
member = list(map(int, input().split()))
member.sort()
cnt = 0
result = 0
for i in member:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0
print(result)

