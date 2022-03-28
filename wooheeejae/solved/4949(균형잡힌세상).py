import sys
input = sys.stdin.readline

while True:
    S = input()
    tempList = []

    # . 만 입력할 시 프로그램 종료
    if S[0] == '.':
        break

    for i in S:
        if i == '[' or i == '(':
            tempList.append(i)
        elif i == ']':
            if len(tempList) > 0 and tempList[-1] == '[':
                tempList.pop()
            else:
                tempList.append(']')
                break
        elif i == ')':
            if len(tempList) > 0 and tempList[-1] == '(':
                tempList.pop()
            else:
                tempList.append(')')
                break

    # tempList에 괄호가 하나라도 남아있다면 짝이 안맞거나 순서가 안맞았을 경우
    if len(tempList) == 0:
        print('yes')
    else:
        print('no')