# 뒤집기
# 0과 1로 이루어진 배열
# 연속된 수 한번에 뒤집을 수 있다.
# 가장 최소로 뒤집어서 가장 작은 수로 뒤집어 모두 같은 수로 만들기

# 내 생각
# 0으로 이루어진 그룹수, 1로 이루어진 그룹수를 count 해서, 더 작은수가 가장 적은 행동

data = input()

# O로 이루어진 그룹의 수 count
zero = 0
# 1로 이루어진 그룹의 수 count
one = 0
ex = data[0]
#
# # 이전 수 저장해서, 바뀌는 경우 -> 이전 수의 group 수 +1
# for i in range(1,len(data)):
#     # 이전 수랑 같으면 pass, 이전 수랑 같지만, 마지막인 경우 update
#     if ex == data[i]:
#         continue
#     # 다른 경우 해당 숫자의 그룹 수 +1
#     else:
#         if ex == '0':
#             zero += 1
#         else:
#             one += 1
#     ex = data[i]
#
# # 마지막 수에 대해 처리
# if ex == '0':
#     zero += 1
# else:
#     one += 1

# 처음 수 부터, 그룹 수 count
if data[0] == '0':
    zero +=1
elif data[0] == '1':
    one += 1

for i in range(len(data) -1):
    if data[i] != data[i+1]:
        if data[i+1] == '0':
            zero += 1
        elif data[i+1] == '1':
            one += 1
# 두 그룹 중 작은 그룹 수
print(min(zero,one))
