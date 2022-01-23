from collections import deque

string = input()

def print_stack(stack): #stack에 넣은 문자열을 출력하는 함수, 반복되서 함수로 만들어줌
    while stack:
        for i in range(len(stack) - 1, -1, -1):
            print(stack[i], end="")
            stack.pop()

def reverse_string(string):
    stack = []
    q = deque(string) #문자열 그대로 deque에 넣으면 원소단위로 분해되서 들어간다.
    while q:
        temp = q.popleft() #맨 앞에 원소를 pop한다.
        if stack and temp == "<": #만약에 pop한게 <임과 동시에, stack에 쌓여있으면 먼저 출력해줘야함
            print_stack(stack)
        if temp == "<": #pop된게 < 라면(stack은 비워진상태)
            print(temp, end = "") #일단 < 출력해줌
            while q: #q에 원소가 있는동안
                _temp = q.popleft() #맨 앞에 원소 pop
                if _temp == ">": #그게 > 라면
                    print(_temp, end ="") # >출력해주고 멈춤
                    break
                else: #아니라면 원소 일단 출력해줌
                    print(_temp, end="")

        elif temp != " ": #만약에 공백이 아니면 stack에 넣어준다
            stack.append(temp)
        else: #공백이라면
            print_stack(stack) #stack원소 출력후
            print(temp, end = "")#공백 추가해줌
    print_stack(stack) #q는 비어있지만 stack에 남아있는 원소들 출력해줘야함

reverse_string(string)