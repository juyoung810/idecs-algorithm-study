import sys

input = sys.stdin.readline

N, M = map(int, input().split())


def find_line():
    start = 0
    end = len(line) - 1
    # 선분 내 가장 왼쪽 index
    while start <= end:
        left = (start + end ) //2
        if l <= line[left] <= r:
            end = left - 1 # 가장 왼쪽 점을 구해야 하므로
        else:
            if line[left] < l:
                start = left + 1
            elif line[left] > r:
                end = left -1

    start = 0
    end = len(line) - 1
    # 선분 내 가장 오른쪽 index
    while start <= end:
        right = (start + end) // 2
        if l <= line[right] <= r:
            start = right + 1  # 가장 왼쪽 점을 구해야 하므로
        else:
            if line[right] < l:
                start = right + 1
            elif line[right] > r:
                end = right - 1

    # 가장 오른쪽 점과 왼쪽 점이 선분 내부에 있는 경우
    if l <= line[left] and line[right] <= r:
        print(right - left + 1)
    # 가장 오른쪽 점과 가장 왼쪽 점이 선분을 벗어난 경우
    elif line[left] < l and r < line[right]:
        print(right - left + 1)
    # 둘 중 하나만 선분 내부에 있는 경우
    else:
        print(right - left)


line = list(map(int, input().rstrip().split()))
line.sort()
print(line)
for _ in range(M):
    l, r = map(int, input().split())
    find_line()
