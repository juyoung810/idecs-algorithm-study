import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def find_title():
    start = 0
    end = len(title) - 1
    result = title[0]
    while start <= end:
        mid = (start + end) // 2
        status = value[mid]
        if one <= status:
            end = mid - 1
            result = title[mid]
        else:
            start = mid + 1
    print(result)


title = []
value = []
for _ in range(N):
    name, num = input().split()
    title.append(name)
    value.append(int(num))

for _ in range(M):
    one = int(input())
    find_title()
