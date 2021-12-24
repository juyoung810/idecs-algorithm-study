# 성적이 낮은 순서로 학생 출력하기

N = int(input())
array = []
for i in range(N):
    input_data = input().split()
    print(input_data)
    array.append((input_data[0],int(input_data[1])))

# key 이용해서 점수 기준 정렬
array = sorted(array, key = lambda student:student[1])
# for _ in range(N):
#     array.append((input().split()))
#
#
# def setting(data):
#     return int(data[1])


# result = sorted(array, key = setting)

for i in array:
    print(i[0], end = " ")

