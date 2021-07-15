import sys
N = int(sys.stdin.readline())

meeting = []

for i in range(N):
    start,end = (map(int,sys.stdin.readline().split(" ")))
    meeting.append([start,end])

## 회의 시간 순 정렬
meeting.sort(key = lambda x:x[0])
#print(meeting)
meeting.sort(key = lambda x:x[1])
#print(meeting)
# meeting.sort(key = lambda x:x[1])
# print(meeting)

end_time = 0
count = 0
for i,j in meeting:
    if i >= end_time:
        count+=1
        end_time = j


sys.stdout.write(str(count))

