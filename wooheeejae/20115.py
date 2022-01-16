#에너지 드링크
 # 기본 변수 설정
drinkNum = int(input())
drinkQaun = list(map(int, input().split()))
answer = 0

 # 문제 풀이
drinkQaun.sort()

for i in range(drinkNum - 1):
    answer += drinkQaun[i] / 2

answer += drinkQaun[-1]

print(answer)