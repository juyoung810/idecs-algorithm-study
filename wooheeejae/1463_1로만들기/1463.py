#####

#1로 만들기
 # 기본 변수 설정
num = int(input())
answer = [0] * (num + 1)

 # 문제 풀이
for i in range(2, num+1):
    answer[i] = answer[i-1] + 1
    if i % 3 == 0:
        answer[i] = min(answer[i], answer[i//3] + 1)
    if i % 2 == 0:
        answer[i] = min(answer[i], answer[i//2] + 1)

print(answer[num])
