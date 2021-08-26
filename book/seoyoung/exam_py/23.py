'''
< 국영수 >
문제 주소 : https://www.acmicpc.net/problem/10825

학생 n명의 이름과 국어, 영어, 수학 점수가 주어질 때, 다음과 같은 조건으로 학생의 성적을 정렬하라.
- 국어 점수가 감소하는 순서
- 국어 점수가 같으면 영어 점수가 증가하는 순서
- 국어, 영어 점수가 같으면 수학 점수가 감소하는 순서
- 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서
- 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서

### 문제 해결 방향
- 간단한 오름차순 정렬은 sorted() 함수로 할 수 있다.
- operator 모듈 함수의 itemgetter(), attrgetter(), methodcaller() 함수를 이용한다
    attrgetter() : 어트리뷰트 꺼냄.
    itemgetter() : 인덱스? 꺼냄
- 복잡한 정렬. 학생 데이터를 grade 내림차순 정렬 후 age의 오름차순으로 정렬하려면, 먼저 age 정렬 수행 후 grade를 사용하여 다시 정렬
    s = sorted(student_objects, key=attrgetter('age'))
    sorted(s, key=attrgetter('grade'), reverse=True)
- 다중 패스로 정렬하기 위해 필드와 순서의 튜플 리스트를 받을 수 있는 래퍼 함수로 추상화 가능
    def multisort(xs, specs):
        for key, reverse in reversed(specs):
            xs.sort(key=attergetter(key), reverse=reverse)
        return xs

    multisort(list(student_objects),(('grade',True),('age',False)))
'''

from operator import itemgetter

# 입력 받기
n = int(input())    # 학생 수 n

# 이름, 국어, 영어, 수학 점수 받기
student = []
for _ in range(n):
    name, kor, eng, math = input().split()
    student.append((name, int(kor), int(eng), int(math)))

def multisort(goal, specs):
    for idx, reverse in reversed(specs):
        goal.sort(key=itemgetter(idx), reverse=reverse)
    return goal

multisort(student, ((1, False), (2, True), (3, False), (0, True)))

for stu_info in student:
    print(stu_info(0))
