 # 기본 변수 설정
# import sys
# input = sys.stdin.readline

num = int(input())
answer = {}

 # 문제 풀이
for i in range(num):
    # 파일명 지정 후 "." 뒤에 확장자만 따옴
    ext = input().split('.')[1]
    if ext in answer.keys():
        answer[ext] += 1
    else:
        answer[ext] = 1
 # 키를 기준으로 오름차순 정렬
 # 값을 기준으로 : sorted(answer.itmes(), key=lambda item: item[1])
ansSort = list(answer.keys())
ansSort.sort()

for i in ansSort:
    print(i, answer[i])



