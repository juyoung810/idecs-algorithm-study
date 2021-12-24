# 0 ~ 9로 이루어진 문자열
# + 혹은 * 가능
# 연산자 우선 순위 고려하지 않는다.
# 가장 큰 수 만들기

# 처음한 생각
# 결과 + 현재 수 VS 결과 * 현재수 더 큰 것 결과로 갱신

# 답
# 결과 또는 현재 수가 0,1이면 더하기가 크고, 2 이상이면 곱하는게 크다.

import sys
input = sys.stdin.readline

array = list(input().rstrip())

# result = 이전 연산의 결과 저장

# 0 번째 숫자 먼저 저장
result = int(array[0])
#
# # 이전의 결과에 다음 수를 + 하는게 큰지 * 하는게 큰지 정해서 결과 갱신
# for idx in range(1,len(array)):
#     if result + int(array[idx]) < result * int(array[idx]):
#         result = result * int(array[idx])
#     else:
#         result = result + int(array[idx])
#

for idx in range(1,len(array)):
    num = int(array[idx])
    if result <= 1 or num <=1:
        result += num
    else:
        result *= num

print(result)