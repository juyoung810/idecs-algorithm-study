#입력세팅
cnt = 0
start = 0
n = int(input())
meeting_info = []
for i in range(n):
    meeting_info.append(list(map(int, input().split())))

meeting_info = sorted(meeting_info, key = lambda x : [x[1], x[0]]) # 끝나는 시간 짧은순으로 정렬
for meeting in meeting_info:
    if meeting[0] >= start:
        start = meeting[1]
        cnt += 1

print(cnt)
