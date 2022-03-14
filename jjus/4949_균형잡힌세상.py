'''
- 모든 경우를 따져서 구현
- (,[ 을 스택에 넣고, )의 경우 직전에 (가, ]의 경우 [가 직전에 있어야함을 이용
- "." 일 경우 중지, 잘 마쳤을 경우 , 스텍에 아무것도 없는데 ),]이 들어온 경우를 고려해야한다.
'''
import sys
input = sys.stdin.readline

arr = []
arr = list(input().rstrip())
while arr[0] != ".":
    state = True
    balance = []
    for i in arr:
        if i == "(" or i == "[":
            balance.append(i)
        elif i == ")":
            if len(balance) == 0 or balance.pop() != "(":
                state = False
                break
        elif i == "]":
            if len(balance) == 0 or balance.pop() != "[":
                state = False
                break
    if len(balance) != 0: state = False
    if state:
        print("yes")
    else:
        print("no")
    arr = list(input().rstrip())