# 알파벳 대문자와, 숫자 (0~9) 로만 구성된 문자열 주어짐
# 알파벳 대문자 오름차순 정렬  + 숫자 합 출력

# 내 생각

# 문자열 오름차순으로 저장하기 위해 입력 받은 문자열을 정렬한다.
# 입력 받은 문자열을 각각 ord() 함수를 통해 아스키 코드로 변환한다.
# A = 65 이므로, 65 보다 작은 경우 숫자합
# 65 이상이면 문자이므로 문자열 합
#
# array = list(input())
# array.sort()
# num_sum = 0
# alpa = ""
# for x in array:
#     if ord(x) < 65:
#         num_sum += int(x)
#     else:
#         alpa += x
#
# print(alpa, end = "")
# print(num_sum)

# 풀이
# 문자 하나씩 확인하면서, 알파벳인 경우 결과 리스트에 넣고 -> isalpha() 함수 사용
# 숫자 따로 더하기
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)
# 알파벳 오름차순 정렬
result.sort()

# 숫자 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
print(''.join(result))



