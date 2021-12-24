# 국어 점수 감소 순
# 국어 점수 같으면 영어 점수 증가 순
# 국 = 영, 수학 감소 순
# 모든 점수 같으면 이름 사전 순 증가


import sys

input = sys.stdin.readline


n = int(input())

# 이름, 국어, 영어, 수학 점수 순 입력 받기
# data = [['J', 50, 60, 100],
#         ['Sangk', 80, 60, 50],
#         ['Sun ', 80, 70, 100],
#         ['Soo', 50, 60, 90],
#         ['H', 50, 60, 100],
#         ['K', 60, 80, 100],
#         ['D', 80, 60, 100],
#         ['Sei', 70, 70, 70],
#         ['W', 70, 70, 90],
#         ['Sangh', 70, 70, 80],
#         ['nsj', 80, 80, 80],
#         ['T', 50, 60, 90, ]]
data = []
for _ in range(n):
    temp = list(input().split())
    # 점수는 int로 변형
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    data.append(temp)


data.sort(key=lambda x: x[0])
print(data)
data.sort(key=lambda x: x[3], reverse=True)
print(data)
data.sort(key=lambda x: x[2])
print(data)
data.sort(key=lambda x: x[1], reverse=True)




for d in data:
    print(d[0])
