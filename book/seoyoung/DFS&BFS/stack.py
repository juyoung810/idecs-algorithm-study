# 스택은 선입후출/후입선출 구조. 나중에 들어온 게 먼저 나간다

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)   # 최하단 원소부터 출력
print(stack[::-1])  # 최상단 원소부터 출력

# 파이썬에서 스택 이용시 별도의 라이브러리 사용할 필요 X
# append = push, pop = pop 메서드 이용시 스택 자료구조와 동일하게 동작