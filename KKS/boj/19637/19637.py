import sys

input = sys.stdin.readline
N, M = map(int, input().split())


def print_tag(stat, tags):
    low = 0
    high = len(tags) - 1
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if int(tags[mid][1]) >= stat:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    return ans


tags = [input().split() for _ in range(N)]

for _ in range(M):
    stat = int(input().rstrip())
    ans = print_tag(stat, tags)
    print(tags[ans][0])
