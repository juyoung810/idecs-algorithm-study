'''
< 곱하기 혹은 더하기 >
각 자리가 숫자로만 이루어진 문자열 s가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어
결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하라
0을 만나면 더하고 나머지는 곱한다. 0을 만나면 그냥 연산을 pass 한다!
!! 1을 생각 안했다. 0이나 1을 만나면 더해준다
'''

s = list(input())
result = int(s[0])

for i in range(1, len(s)):
    if int(s[i]) <= 1 or result <= 1:
        result += int(s[i])
    else:
        result *= int(s[i])

print(result)