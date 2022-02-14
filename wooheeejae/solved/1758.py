#알바생 강호
 # 기본 변수 설정
peopleNum = int(input())
peopleTip = []
answer = 0

for j in range(peopleNum):
    peopleTip.append(int(input()))

 # 문제 풀이
peopleTip.sort(reverse=True)
for i in range(peopleNum):
    peopleTip[i] = peopleTip[i] - i
    if peopleTip[i] <= 0:
        peopleTip[i] = 0
    answer += peopleTip[i]

print(answer)

