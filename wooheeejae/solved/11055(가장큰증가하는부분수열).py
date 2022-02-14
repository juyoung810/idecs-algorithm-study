 # 기본 변수 설정
n = int(input())
numList = list(map(int, input().split()))

 # 문제 풀이
temp = [1] * n # n번째 자리를 기준으로 증가하는 부분을 더했을 때 값
temp[0] = numList[0]

for i in range(1, n): # 0번 인덱스는 비교할 필요 없음
    for j in range(i):
        # i번째 인덱스를 기준으로 그 전에 있는 것들과 비교
        # numList[j] < numList[i] : 증가하는 부분일 때
        # temp[j] + numList[i] : j인덱스 까지 증가하는 부분을 더한 것에 자기자신을 더해 계산을 줄임
        if numList[j] < numList[i]:
            temp[i] = max(temp[i], temp[j] + numList[i])
        # 증가하는 부분이 아닐 때 i번째 인덱스 자체가 더큰지 비교
        else:
            temp[i] = max(temp[i], numList[i])

print(max(temp))