#거스름돈
 # 기본 변수 설정
answer = 0
inputNum = int(input())

rmd5 = inputNum % 5 # 나머지
share5 = inputNum // 5 # 5로 나눈 몫

 # 문제 풀이

 # 나눌 수 없는 경우
if inputNum == 1:
    print(-1)
elif inputNum == 3:
    print(-1)

 # 500원짜리 최대인 경우
elif rmd5 % 2 == 0:
    answer = share5 + (rmd5 // 2)
    print(answer)

 # 500원짜리 (최대-1)인 경우
else:
    share5 -= 1
    rmd5 += 5
    share2 = rmd5 // 2 # 2로 나눈 몫
    answer = share2 + share5
    print(answer)
