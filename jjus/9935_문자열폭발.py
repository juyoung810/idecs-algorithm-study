import sys
input = sys.stdin.readline

in_str = input().rstrip()
key = input().rstrip()
stack = []

for i in range(len(in_str)):
    stack.append(in_str[i])
    # stack의 끝 과 key 문자열 끝이 같을 경우
    # stack의 끝 ~ key 문자열 길이 만큼이 key와 같은 경우 폭발
    if stack[-1] == key[-1] and ''.join(stack[-len(key):]) == key:
        del stack[-len(key):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')