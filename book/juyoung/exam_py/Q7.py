# 럭키 스트레이트
# 짝수 자릿수 주어지면, 반 나눠서 더한 수 서로 같으면 기술 사용 가능

# 문자열 배열로 입력 받기
grade = list(input())

# 좌 저장 , 우 저장
left = 0
right = 0

for i in range(len(grade)//2):
    left += int(grade[i])


for i in range(len(grade)//2,len(grade)):
    right += int(grade[i])

if left == right:
    print("LUCKY")
else:
    print("READY")

