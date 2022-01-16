#주유소
 # 기본 변수 설정
gasNum = int(input())
gasDistance = list(map(int, input().split()))
gasPrice = list(map(int, input().split()))
answer = 0

 # 문제 풀이
tempPrice = gasPrice[0]
for i in range(gasNum-1):
    if gasPrice[i] < tempPrice:
        tempPrice = gasPrice[i]
    answer += tempPrice * gasDistance[i]

print(answer)
