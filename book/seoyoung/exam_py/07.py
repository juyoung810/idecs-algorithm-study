'''
< 럭키 스트레이트 >
게임 내에서 점수가 특정 조건을 만족할 때만 사용할 수 있는 기술.
- 현재 캐릭터의 점수를 N이라고 할 때 자릿수를 기준으로 점수 N을 반으로 나누어 왼쪽 부분의 각 자릿수의 합과 오른쪽 부분의 각 자릿수의 합을 더한 값이 동일한 상황
점수의 자릿수는 항상 짝수로 들어온다.

점수가 주어지면 럭키 스트레이트를 사용할 수 있는 상태인지 아닌지 알려주는 프로그램을 작성하라!
그냥 슬라이스를 쓰면 되는게 아닐까!
'''

n = input() # 문자열 형태로 받는다. 슬라이싱 하기 위해서...

middle = len(n) // 2
front = n[:middle]
back = n[middle:]
f = 0
b = 0

for i in range(middle):
    f += int(front[i])
    b += int(back[i])

if f == b:
    print("LUCKY")
else:
    print("READY")

    
# 책 소스코드
n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length // 2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length // 2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")