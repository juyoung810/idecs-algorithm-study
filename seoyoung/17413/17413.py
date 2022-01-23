'''
< 단어 뒤집기 2 >
문자열 S가 주어졌을 때, 이 문자열에서 단어만 뒤집으려 한다.

- 문자열 S의 규칙
1. 알파벳 소문자, 숫자, 공백, 특수문자로만 이루어져 있다.
2. 문자열의 시작과 끝은 공백이 아니다.
3. 부등호가 문자열에 있는 경우 번갈아가면서 등장하며, <이 먼저 등장한다. 또, 두 문자의 개수가 같다.

태그는 <로 시작해서 >로 끝나는 길이가 3 이상인 부분 문자열이고, <> 사이에는 알파벳 소문자와 공백만 있다.
단어는 알파벳 소문자와 숫자로 이루어진 부분 문자열이고, 연속하는 두 단어는 공백 하나로 구분한다.
태그는 단어가 아니며, 태그와 단어 사이에는 공백이 없다.

< 아이디어 >
1. 단어는 공백과 태그로 구분이 가능하다.
2. 태그는 그대로 출력해주어야 한다.
3. 단어의 순서는 유지해주어야 한다.
'''

S = input()
word = ''
result = ''
tag = False

for i in range(len(S)):
    if S[i] == '<':
        result += word[::-1]
        word = ''
        tag = True
        word += '<'
    elif S[i] == '>':
        result += word + '>'
        word = ''
        tag = False
    elif S[i] == ' ' and tag == False:
        word = word[::-1]
        result += word + ' '
        word = ''
    elif S[i] == ' ' and tag == True:
        word += S[i]
    elif i == len(S) - 1:
        word += S[i]
        word = word[::-1]
        result += word
    else:
        word += S[i]

print(result)