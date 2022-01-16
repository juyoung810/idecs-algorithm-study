#####

#로프
 # 기본 변수 설정
ropeNum = int(input())
ropeWeight = []
answer = []

for i in range(ropeNum):
    ropeWeight.append(int(input()))

 # 문제 풀이
ropeWeight.sort(reverse=True)

for j in range(ropeNum):
    answer.append(ropeWeight[j] * (j+1))

print(max(answer))
