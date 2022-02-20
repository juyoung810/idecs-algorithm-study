N = int(input())
cnt = 0
start = 0
meeting = []

for i in range(N):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key = lambda x : [x[1], x[0]])

for meet in meeting:
    if meet[0] >= start:
        start = meeting[1]
        cnt += 1

print(cnt)
