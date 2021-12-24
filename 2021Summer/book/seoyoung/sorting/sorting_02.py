### 성적이 낮은 순서로 학생 출력하기
## 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름 출력하기 (정렬 라이브러리 key 사용하면 될 듯)

# 학생 수
n = int(input())

# 학생 이름, 성적 공백으로 구분되어 입력
array = []

for i in range(n):
    student = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((student[0], int(student[1])))   # 튜플로 저장

# 키를 이용해 점수 기준 정렬
array = sorted(array, key=lambda student: student[1])   # 키에는 함수를 넣어줘야 함. 람다 함수 이용

# 정렬이 수행된 결과 출력
for student in array:
    print(student[0], end=' ')
