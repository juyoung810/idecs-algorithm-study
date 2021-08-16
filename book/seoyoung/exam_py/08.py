'''
< 문자열 재정렬 >
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력한다.

알파벳을 받으면 유니코드로 변환해서 정렬한 후 다시 바꿔서 출력해주기
숫자는 더해주기
'''

s = input()
alphabet = []
num = 0

for i in s:
    if ord(i) in range(48, 58): # 이건 유니코드를 알 수 없으면 못 쓰니까 썩 좋은 방법은 아닌 것 같기도
        num += int(i)
    else:
        alphabet.append(ord(i))

alphabet.sort()
result = ''
for i in alphabet:
    result += chr(i)

if num != 0:
    result += str(num)

print(result)


# 책 소스코드. 알파벳인지 확인하는 함수가 있었다! 이런젠장
data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬(알파벳도 정렬 되는지 몰랐다)
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입(이걸 놓침)
if value != 0:
    result.append(str(value))

# 최종 결과 출력
print(''.join(result))