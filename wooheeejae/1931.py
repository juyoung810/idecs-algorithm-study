#####

#회의실 배정
 # 기본 변수 설정
meetNum = int(input())
meetTime = []
answer = 1

for i in range(meetNum):
    one, two = map(int, input().split())
    #two = map(int, input().split())
    meetTime.append([one, two])

 # 문제 풀이
meetTime.sort(key = lambda x: x[0])
meetTime.sort(key = lambda x: x[1])

endTime = meetTime[0][1]
for i in range(1, meetNum):
    if meetTime[i][0] >= endTime:
        answer += 1
        endTime = meetTime[i][1]

print(answer)
